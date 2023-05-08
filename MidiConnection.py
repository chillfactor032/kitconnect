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

    def __init__(self, io_port_name, recv_msg_callback=None):
        super(MidiConnection, self).__init__()
        
        self.io_port_name = io_port_name
        self.port = None
        self.recv_msg_callback = recv_msg_callback
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
        while not self.stopped:
            time.sleep(0.001)
            msg = self.port.poll()
            if msg:
                self.recv_msg_callback(msg)
        self.port.close()

    def stop(self):
        self.stopped = True

    @staticmethod
    def get_devices():
        devices = mido.get_ioport_names()
        devices.append("TestPort")
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
        msgs = [
            mido.Message("note_on", note=60),
            mido.Message("program_change", program=67),
            mido.Message("note_off", note=60)
        ]   
        return random.choice(msgs)
    
    def callback_monitor(self):
        while not self.closed:
            time.sleep(random.random()*3)
            msg = self.random_msg()
            print(f"TestPort Send: [{msg}]")
            self.callback(msg)

    def _open(self):
        print("TestPort Opened")

    def _close(self):
        self.closed = True
        if self.callback is not None:
            self.callback_thread.join()
        print("TestPort Closed")

    def _send(self, msg):
        print(f"TestPort Recv: [{msg}]")

    def _receive(self, block=True):
        time.sleep(random.random()*3)
        msg = self.random_msg()
        print(f"TestPort Send: [{msg}]")
        return None

    
