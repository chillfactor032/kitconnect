#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Python Imports
import sys
import os
import time
import pygame.midi
from enum import Enum

#PySide6 Imports
from PySide6.QtCore import QRunnable, Signal, Slot, QObject

#Log Levels
class LogLevel(Enum):
    INFO = 0
    ERROR = 10
    DEBUG = 20
    
class TD50X(QRunnable):

    MODEL_TD50X =  [0, 0, 0, 0, 7]
    COMMAND_RQ1 = 0x11
    STATUS_SYSEX = 0xF0
    STATUS_EOX = 0xF7
    STATUS_TIMING_CLOCK = 0xF8
    STATUS_PROGRAM_CHANGE = 0xC9
    VENDOR_ID_ROLAND = 0x41
    DEVICE_ID = 0x10
    TARGET_DEVICE_NAME = "TD-50X"

    class Signals(QObject):
        done = Signal(bool)
        log = Signal(str, LogLevel)
        #Midi Msg TYPE, Incoming, Msg Data
        midi_msg = Signal(int, bool, list)

    def __init__(self, td50x_id=None):
        super(TD50X, self).__init__()
        if td50x_id is None:
            self.td50x_id = TD50X.DEVICE_ID
        else:
            self.td50x_id = td50x_id
        self.input_device_id = -1
        self.output_device_id = -1
        self.output_device = None
        self.input_device = None
        self.stopped = False
        self.outbox = []
        self.update = True
        self.signals = self.Signals()
        pygame.midi.init()
    
    @staticmethod
    def to_str(msg):
        new_msg = []
        for x in range(0, len(msg)):
            new_msg.append(hex(msg[x]))
        return new_msg
    
    def set_input_device(self, device_id):
        self.input_device_id = device_id

    def set_output_device(self, device_id):
        self.output_device_id = device_id

    def set_device_id(self, device_id):
        self.td50x_id = device_id

    def get_devices(self):
        devices = []
        num_midi_devices = pygame.midi.get_count()
        self.signals.log.emit(f"Found {num_midi_devices} MIDI devices", LogLevel.INFO)
        input_device_id = None
        output_device_id = None
        for x in range(num_midi_devices):
            device_info = pygame.midi.get_device_info(x)
            device = {
                "name": "",
                "input_id": -1,
                "output_id": -1,
                "desc": ""
            }
            if not device_info:
                continue
            iface, dname, is_input, is_output, opened = device_info
            device["name"] = dname.decode(encoding="UTF-8")
            if is_input:
                device["input_id"] = x
            if is_output:
                device["output_id"] = x
            self.signals.log.emit(f"  [{x}] [{device['name']}] {is_input} {is_output}", LogLevel.DEBUG)
            # Look for other devices with the same name
            for y in range(x+1,num_midi_devices):
                device_info = pygame.midi.get_device_info(y)
                if not device_info:
                    continue
                iface, dname, is_input, is_output, opened = device_info
                if device["name"] == dname.decode(encoding="UTF-8"):
                    #Found a matching Device Name
                    if is_input:
                        device["input_id"] = y
                    if is_output:
                        device["output_id"] = y
            devices.append(device)

        #Create the "Descriptions"
        for device in devices:
            device["desc"] = device["name"]
            # 4 Possibilities
            #   Output Only
            if device["input_id"] < 0 and device["output_id"] >= 0:
                device["desc"] += " (output)"
            #   Input Only
            if device["input_id"] >= 0 and device["output_id"] < 0:
                device["desc"] += " (input)"
            #   Input + Output
            if device["input_id"] >= 0 and device["output_id"] >= 0:
                device["desc"] += " (input + output)"
            #   No Input or Output?
            if device["input_id"] < 0 and device["output_id"] < 0:
                device["desc"] += " (No Input or Output - Invalid Device)"
        print(devices)
        return devices
            

    def is_connected(self):
        pass
    
    def update_devices(self, input_device_id, output_device_id):
        self.input_device_id = input_device_id
        self.output_device_id = output_device_id
        self.update = True

    def send_msg(self, msg):
        self.outbox.append(msg)

    def stop_midi(self):
        self.stopped = True

    #Handle an incoming message
    def handle_msg(self, msg, timestamp):
        self.signals.midi_msg.emit(0, True, msg)
        print(f'{[f"{d:02x}" for d in msg]} {timestamp * 1e-3 : .3f}')

    @Slot()
    def run(self):
        if self.input_device_id < 0 or self.output_device_id < 0:
            self.signals.log.emit("Midi device not set.", LogLevel.INFO)
            return
        self.input_device = pygame.midi.Input(self.input_device_id)
        self.output_device = pygame.midi.Output(self.output_device_id)
        sysex_response_buffer = None
        self.signals.log.emit("TD-50X Midi Client Started", LogLevel.INFO)
        while self.stopped == False:
            #If devices have changed, update
            if self.update:
                self.signals.log.emit("Updating Midi Devices", LogLevel.INFO)
                self.output_device.abort()
                self.output_device.stop()
                self.input_device.close()
                self.input_device = pygame.midi.Input(self.input_device_id)
                self.output_device = pygame.midi.Output(self.output_device_id)
                self.signals.log.emit(f"Updated midi devices to in=[{self.input_device}] out=[{self.output_device_id}]", LogLevel.DEBUG)
                self.update = False
                
            #If no devices specified just do nothing
            if self.input_device < 0 or self.output_device < 0 or self.input_device is None or self.output_device is None:
                time.sleep(0.01)
                continue

            #Write a message from the outbox if its there
            if len(self.outbox) > 0:
                self.signals.midi_msg.emit(0, False, self.outbox[0])
                if self.outbox[0][0] == TD50X.STATUS_SYSEX:
                    self.signals.log.emit("Sending SysEx Msg: " + TD50X.to_str(self.outbox[0]), LogLevel.DEBUG)
                    self.output_device.write_sys_ex(0, self.outbox[0])
                else:
                    self.signals.log.emit("Sending Midi Msg: " + TD50X.to_str(self.outbox[0]), LogLevel.DEBUG)
                    self.output_device.write([[self.outbox[0], 0]])

            #Read Some Events
            event_list = pygame.midi.Input.read(self.input_device, 16)
            for event in event_list:
                data, timestamp = event
                if sysex_response_buffer is not None:
                    sysex_response_buffer.extend(data)
                    if TD50X.STATUS_EOX in data:
                        self.handle_msg(sysex_response_buffer, timestamp)
                        sysex_response_buffer = None
                elif data[0] == TD50X.STATUS_SYSEX:
                    #Begin recv a sysex msg
                    sysex_response_buffer = data
                elif data[0] == TD50X.STATUS_TIMING_CLOCK:
                    continue  # clock sync message
                else:
                    #Handle one-packet msg
                    self.handle_msg(data, timestamp)

        #Clean up if stopped
        self.output_device.abort()
        self.output_device.stop()
        self.input_device.close()
        self.signals.log.emit("TD-50X Midi Client Stopped", LogLevel.INFO)
        



    
