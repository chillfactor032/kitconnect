#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#Python Imports
from threading import Thread
import mido
from mido.ports import BaseIOPort
import time
import random

mido.set_backend('mido.backends.pygame')

class MidiConnection(Thread):

    def __init__(self, io_port_name, recv_msg_callback=None, connected_callback=None):
        super(MidiConnection, self).__init__()
        self.io_port_name = io_port_name
        self.port = None
        self.recv_msg_callback = recv_msg_callback
        self.connected_callback = connected_callback
        self.stopped = False

    def send_msg(self, msg):
        if self.port is None or self.port.closed:
            return
        self.port.send(msg)

    def run(self):
        if self.io_port_name == "TestPort":
            self.port = TestPort()
        else:
            self.port = mido.open_ioport(self.io_port_name)
        if self.port and self.connected_callback is not None:
            self.connected_callback()
        while not self.stopped:
            time.sleep(0.0001)
            msg = self.port.poll()
            if msg:
                self.recv_msg_callback(msg)
        self.port.close()

    def stop(self):
        self.stopped = True

    @staticmethod
    def get_devices():
        devices = mido.get_ioport_names()
        return devices
        
class TestPort(BaseIOPort):
    
    def __init__(self, callback=None):
        super(BaseIOPort, self).__init__()
        self.name = "Test Port"
        self.closed = False
        self.callback = callback
        if callback:
            self.callback_thread = Thread(target=self.callback_monitor)
            self.callback_thread.start()

    def random_msg(self):
        msg = None
        r = random.random()
        drums = [36,38,48,42,46,49]
        kit_chng = [
            mido.Message('sysex', data=[65,16,0,0,0,0,7,18,4,36,0,0,76,117,100,119,105,103,32,83,117,112,114,97,72,121,98,114,105,100,32,32,32,32,32,32,32,32,76]),
            mido.Message('sysex', data=[65,16,0,0,0,0,7,18,4,56,0,0,83,116,97,114,32,66,117,98,105,110,103,97,87,97,108,110,117,116,32,32,32,32,32,32,32,32,76]),
            mido.Message('sysex', data=[65,16,0,0,0,0,7,18,4,76,0,0,65,105,114,70,114,111,109,26,65,115,105,97,84,97,98,108,97,32,32,32,32,32,32,32,32,32,32,32,76])
        ]
        notes = [
            mido.Message("note_on", note=38),
            mido.Message("note_off", note=38)
        ]
        other = [
            mido.Message("program_change", program=random.randint(0,99)),
            mido.Message("polytouch", note=49, value=random.randint(0,127)),
            mido.Message("control_change", control=4, value=random.randint(0,127))
        ]
        if r > 0.9:
            msg = random.choice(kit_chng)
        elif r > 0.6:
            msg = random.choice(other)
        else:
            msg = random.choice(notes)
            msg.note = random.choice(drums)
        return msg
    
    def callback_monitor(self):
        while not self.closed:
            time.sleep(random.random()*0.6)
            msg = self.random_msg()
            #print(f"TestPort Send: [{msg}]")
            self.callback(msg)

    def _open(self):
        #print("TestPort Opened")
        pass

    def _close(self):
        self.closed = True
        if self.callback is not None:
            self.callback_thread.join()
        #print("TestPort Closed")

    def _send(self, msg):
        #print(f"TestPort Recv: [{msg}]")
        pass

    def _receive(self, block=False):
        msg = self.random_msg()
        #print(f"TestPort Send: [{msg}]")
        time.sleep(random.random())
        return msg

    
