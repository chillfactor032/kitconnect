#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Python Imports
import sys
import os
import time
import mido
from enum import Enum

#PySide6 Imports
from PySide6.QtCore import QRunnable, Signal, Slot, QObject

from MidiConnection import MidiConnection

class TD50X():

    class Constants():
        ROLAND_ID = 0x41
        MODEL_ID = [0, 0, 0, 0, 7]


    class Status(Enum):
        UNKNOWN = 0
        NOTE_OFF = range(0x80, 0x90)
        NOTE_ON = range(0x90, 0xa0)
        KEY_PRESSURE = range(0xa0, 0xb0)
        CTRL_CHG = range(0xb0, 0xc0)
        PROG_CHG = range(0xc0, 0xd0)
        SYSEX = 0xf0
        EOX = 0xf7
        CLOCK = 0xf8
        START = 0xfa
        ACTIVE_SENSING = 0xfe

        def __eq__(self, other) -> bool:
            if type(self.value) == range:
                return other in self.value
            if type(other) == TD50X.Status:
                return self.value == other.value
            if type(other) == int:
                return self.value == other
            return False

        def base(self):
            if type(self.value) == range:
                return min(self.value)
            return self.value

    class ControlChange(Enum):
        MODULATION = 0x01
        BREATH = 0x02
        FOOT = 0x04
        EXPRESSION = 0x0b
        GENERAL_PURPOSE_1 = 0x10
        GENERAL_PURPOSE_2 = 0x11
        GENERAL_PURPOSE_3 = 0x12
        GENERAL_PURPOSE_4 = 0x13
        GENERAL_PURPOSE_5 = 0x50
        GENERAL_PURPOSE_6 = 0x51
        GENERAL_PURPOSE_7 = 0x52
        GENERAL_PURPOSE_8 = 0x53
        HIGH_VELOCITY_PREFIX = 0x58
        ALL_SOUNDS_OFF = 0x78
        RESET_ALL_CONTROLLERS = 0x79
        ALL_NOTES_OFF = 0x7B
        OMNI_OFF = 0x7C
        OMNI_ON = 0x7D
        MONO = 0x7E
        POLY = 0x7F

    class Command(Enum):
        RQ1 = 0x11
        DT1 = 0x12

    class NoteNumbers(Enum):
        KICK = 36
        SNARE_HEAD = 38
        SNARE_RIM = 40
        SNARE_X_STICK = 37
        TOM_1 = 48
        TOM_1_RIM = 50
        TOM_2 = 45
        TOM_2_RIM = 47
        TOM_3_HEAD = 43
        TOM_3_RIM = 58
        TOM_4_HEAD = 41
        TOM_4_RIM = 39
        HH_OPEN_BOW = 46
        HH_OPEN_EDGE = 26
        HH_CLOSED_BOW = 42
        HH_CLOSED_EDGE = 22
        HH_PEDAL = 44
        CRASH_1_BOW = 49
        CRASH_1_EDGE = 55
        CRASH_2_BOW = 57
        CRASH_2_EDGE = 52
        RIDE_BOW = 51
        RIDE_EDGE = 59
        RIDE_BELL = 53
        AUX_1_HEAD = 27
        AUX_1_RIM = 28
        AUX_2_HEAD = 29
        AUX_2_RIM = 30
        AUX_3_HEAD = 31
        AUX3_RIM = 32
        AUX_4_HEAD = 33
        AUX4_RIM = 34

    def __init__(self, port_name, midi_channel=0x09, device_id=0x10):
        super(TD50X, self).__init__()
        self.kit_id = 0
        self.kit_name = "Not Set"
        self.kit_subname = ""
        self.port_name = port_name
        self.device_id = device_id
        self.midi_channel = midi_channel
        self.midi = MidiConnection(self.port_name,self.recv_msg)

    def set_device_id(self, device_id):
        self.device_id = device_id

    def midi_start(self, test=False):
        self.midi.start()

    def midi_stop(self, wait=True):
        self.midi.stop()
        self.midi.join()

    def refresh_current_kit(self, kit_id=None):
        if not kit_id:
            addr = [0,0,0,0]
            size = [0,0,0,1]
            msg = mido.Message.from_bytes(self.prepare_sysex_msg(addr, size))
            self.send_msg(msg)
        else:
            addr = TD50X.kit_id_to_addr(kit_id)
            size = [0,0,0,28]
            msg = mido.Message.from_bytes(self.prepare_sysex_msg(addr, size))
            self.send_msg(msg)

    # Set the kit to kit number
    # Kit Number is 1-128, not the 0 based kit Id
    def set_kit(self, kit_num=None, relative=0):
        if kit_num is None and relative == 0:
            return
        if kit_num is None:
            kit_id = self.kit_id
        else:
            if kit_num < 1 or kit_num > 100:
                return
            kit_id = kit_num - 1 
        kit_id = (relative+kit_id) % 128
        self.send_msg(mido.Message("program_change", channel=self.midi_channel, program=kit_id))
        self.refresh_current_kit(kit_id)
    
    def send_msg(self, msg):
        self.midi.send_msg(msg)
        print(f"> [{msg}]")

    def recv_msg(self, msg):
        if msg.type == "sysex":
            self.recv_sysex_msg(msg)
        if msg.type == "program_change":
            #Kit has been changed, send kit refresh msg
            self.refresh_current_kit(msg.program)
        if msg.type == "note_on":
            pass
        print(f"< [{msg}]")

    def recv_sysex_msg(self, msg):
        cmd = msg.data[7]
        addr = TD50X.unpack(msg.data[8:12])
        left = self.unpack([4,0,0,0])
        right = self.unpack([5,0x46,0,0])
        if cmd == TD50X.Command.DT1.value and addr == 0:
            # Current Kit Query
            kit_id = msg.data[-2]
            #Update Get Kit Name too
            self.refresh_current_kit(kit_id)
        elif cmd == TD50X.Command.DT1.value and addr >= self.unpack([4,0,0,0]) and addr <= self.unpack([5,0x46,0,0]):
            #Kit Name Query
            self.kit_id = self.addr_to_kit_id(msg.data[8:12])
            self.kit_name = TD50X.list_to_ascii(msg.data[12:25])
            self.kit_subname = TD50X.list_to_ascii(msg.data[25:-2])
            print(f"Current Kit Updated: {self.kit_id+1} - {self.kit_name} - {self.kit_subname}")

    def prepare_sysex_msg(self, addr, size):
        """add the status fields and checksum to the message"""
        msg = TD50X.flatten(
            TD50X.Status.SYSEX.value, 
            TD50X.Constants.ROLAND_ID, 
            self.device_id, 
            TD50X.Constants.MODEL_ID, 
            TD50X.Command.RQ1.value
        )
        payload = []
        payload.extend(addr)
        payload.extend(size)
        msg.extend(payload)
        msg.append(TD50X.checksum(payload))
        msg.append(TD50X.Status.EOX.value)
        return msg

    @staticmethod
    def prepare_sysex_msg2(addr, size):
        """add the status fields and checksum to the message"""
        msg = TD50X.flatten(
            TD50X.Status.SYSEX.value, 
            TD50X.Constants.ROLAND_ID, 
            0x10, 
            TD50X.Constants.MODEL_ID, 
            TD50X.Command.RQ1.value
        )
        payload = []
        payload.extend(addr)
        payload.extend(size)
        msg.extend(payload)
        msg.append(TD50X.checksum(payload))
        msg.append(TD50X.Status.EOX.value)
        return msg
    
    @staticmethod
    def list_to_ascii(lst):
        text = ""
        for char in lst:
            text += chr(char)
        return text
    
    @staticmethod
    def flatten(*args):
        out = []
        for a in args:
            if isinstance(a, list):
                out.extend(a)
            else:
                out.append(a)
        return out

    @staticmethod
    def kit_id_to_addr(kit_id: int):
        base = 4<<21
        step = 2<<14
        return TD50X.pack4(base + kit_id * step)

    @staticmethod
    def addr_to_kit_id(addr: list):
        base = 4<<21
        step = 2<<14
        return int((TD50X.unpack(addr) - base) / step)

    @staticmethod
    def pack4(n):
        out = []
        for i in range(4):
            out.append((n >> 21) & 0x7f)
            n <<= 7
        return out

    @staticmethod
    def unpack(arr: list) -> int:
        out = 0
        for x in arr:
            out = (out << 7) + x
        return out

    @staticmethod
    def checksum(arr):
        sum = 0
        for b in arr:
            sum += b
        return 128 - (sum % 128)
    
    @staticmethod
    def to_str(msg):
        #Get Parse Status Byte
        status = TD50X.Status.UNKNOWN
        byte_list = msg.copy()
        midi_channel = -1
        if len(msg) < 4:
            return ""
        
        # Classify the status byte
        for status_enum in TD50X.Status:
            if status_enum == msg[0]:
                status = status_enum
                byte_list[0] = status.name
                break

        #Based on status byte, parse the midi_channel
        if type(status.value) == range:
            midi_channel = TD50X.get_midi_channel(msg[0])
            byte_list[0] += f"(midi_ch={midi_channel})"

        if status in [TD50X.Status.NOTE_ON, TD50X.Status.NOTE_OFF, TD50X.Status.KEY_PRESSURE]:
            
            #Byte 2 is a note number, translate to drum
            for note_num_enum in TD50X.NoteNumbers:
                if note_num_enum.value == msg[1]:
                    byte_list[1] = note_num_enum.name + f"({note_num_enum.value})"
                    break
        
        if status in [TD50X.Status.NOTE_ON, TD50X.Status.NOTE_OFF]:
            byte_list[2] = f"VELOCITY({msg[2]})"

        if status == TD50X.Status.PROG_CHG:
            #Byte 2 is a kit number
            byte_list[1] = f"KIT({msg[1]+1})"

        if status in TD50X.ControlChange:
            # What kind of control change is it?
            for ctrl__chg_enum in TD50X.ControlChange:
                if ctrl__chg_enum == msg[1]:
                    byte_list[1] = ctrl__chg_enum

        return "["+ ",".join([str(x) for x in byte_list]) +"]"

    @staticmethod
    def get_midi_devices():
        return MidiConnection.get_devices()
    
    @staticmethod
    def to_hex(msg):
        return MidiConnection.to_str(msg)

    @staticmethod
    def get_midi_channel(byte):
        return byte & 0x0f
    
    @staticmethod
    def checksum(msg):
        sum = 0
        for b in msg:
            sum += b
        return 128 - (sum % 128)