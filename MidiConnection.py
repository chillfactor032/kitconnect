#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Python Imports
from threading import Thread
import pygame.midi
import time
import random



class MidiConnection():

    COMMAND_RQ1 = 0x11
    STATUS_SYSEX = 0xF0
    STATUS_EOX = 0xF7
    STATUS_TIMING_CLOCK = 0xF8
    STATUS_PROGRAM_CHANGE = 0xC9

    def __init__(self, input_device_id, output_device_id, recv_msg_callback=None):
        super(MidiConnection, self).__init__()
        self.input_device_id = input_device_id
        self.output_device_id = output_device_id
        self.recv_msg_callback = recv_msg_callback
        self.output_device = None
        self.input_device = None
        self.stopped = False
        self.done = False
        self.test_msgs = []
        self.outbox = []
    
    def handle_msg(self, data, timestamp):
        if self.recv_msg_callback is not None:
            self.recv_msg_callback(data,timestamp)
        else:
            print(f'{[f"{d:02x}" for d in data]} {timestamp * 1e-3 : .3f}')

    def test_recv_msgs(self):
        start = time.time()
        elapsed = 0
        rand = 0
        while not self.stopped:
            rand = random.random()
            #Send a msg from the outbox
            if len(self.outbox) > 0:
                msg = self.outbox.pop(0)
                print("> "+MidiConnection.to_str(msg))
            elapsed = time.time()-start
            if rand > 0.90:
                if len(self.test_msgs) > 0:
                    self.handle_msg(random.choice(self.test_msgs), round(elapsed*1000))
                else:
                    self.handle_msg([random.randint(0,0x7E), random.randint(0,0x7E), random.randint(0,0x7E), random.randint(0,0x7E)], round(elapsed*1000))
            time.sleep(rand)
        self.done = True

    def stop(self):
        self.stopped = True
        if self.thread is not None:
            self.thread.join()

    def start_test(self):
        self.thread = Thread(target=self.test_recv_msgs, daemon=True).start()

    def start(self):
        self.thread = Thread(target=self.run, daemon=True).start()

    def run(self):
        if pygame.midi.get_init() == False:
            pygame.midi.init()
        input_device = pygame.midi.Input(self.input_device_id)
        output_device = pygame.midi.Output(self.output_device_id)
        sysex_response_buffer = None

        while not self.stopped:
            #Sleep for a bit if theres no data and nothing in outbox
            while input_device.poll() == False and len(self.outbox) == 0:
                time.sleep(0.001)
            #Send a msg from the outbox
            if len(self.outbox) > 0:
                evt = self.outbox.pop(0)
                if evt[0] == MidiConnection.STATUS_SYSEX:
                    #Send a SysEx Msg
                    output_device.write_sys_ex(0,evt)
                else:
                    #Send a Msg
                    output_device.write([[evt, 0]])

            #Read Some Events
            event_list = pygame.midi.Input.read(input_device, 16)
            for event in event_list:
                data, timestamp = event
                if sysex_response_buffer is not None:
                    sysex_response_buffer.extend(data)
                    if MidiConnection.STATUS_EOX in data:
                        self.handle_msg(sysex_response_buffer, timestamp)
                        sysex_response_buffer = None
                elif data[0] == MidiConnection.STATUS_SYSEX:
                    #Begin recv a sysex msg
                    sysex_response_buffer = data
                elif data[0] == MidiConnection.STATUS_TIMING_CLOCK:
                    continue  # clock sync message
                else:
                    #Handle one-packet msg
                    self.handle_msg(data, timestamp)
        self.done = True

    #Add a msg to the outbox
    def send_msg(self, msg):
        self.outbox.append(msg)

    def wait(self, timeout=3):
        start = time.time()
        elapsed = 0
        while elapsed < timeout and self.done == False:
            time.sleep(0.001)
    
    @staticmethod
    def to_str(msg):
        return "["+", ".join(f"{b:#0{4}x}" for b in msg)+"]"
    
    @staticmethod
    def get_devices():
        devices = []
        if pygame.midi.get_init() == False:
            pygame.midi.init()
        num_midi_devices = pygame.midi.get_count()
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
        return devices
        



    
