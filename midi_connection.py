"""
MidiConnection controls the i/o messages to a midi port
TestPort is a virtual midi port for testing
"""
import queue
import time
import random
from threading import Thread
from os import environ
import mido

#Suppress the hello message from PyGame
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
mido.set_backend('mido.backends.pygame')

class MidiConnection(Thread):
    """Controls the i/o messages to a midi port"""
    def __init__(self, io_port_name, recv_msg_callback=None, connected_callback=None):
        super(MidiConnection, self).__init__()
        self.io_port_name = io_port_name
        self.port = None
        self.msg_queue = queue.SimpleQueue()
        self.recv_msg_callback = recv_msg_callback
        self.connected_callback = connected_callback
        self.stopped = False

    def send_msg(self, msg):
        """Put a Midi Message on the Outbound Queue"""
        self.msg_queue.put(msg)

    def run(self):
        """Start the I/O Thread"""
        if self.io_port_name == "TestPort":
            self.port = TestPort()
        else:
            self.port = mido.open_ioport(self.io_port_name)
        if self.port and self.connected_callback is not None:
            self.connected_callback()
        while not self.stopped:
            time.sleep(0.00001)
            # Check if message has been recv
            msg = self.port.poll()
            if msg:
                self.recv_msg_callback(msg)
            # Check if there is an outgoing msg in queue
            if not self.msg_queue.empty():
                msg = self.msg_queue.get_nowait()
                self.port.send(msg)
        self.port.close()

    def stop(self):
        """Tell the MidiConnection thread to stop"""
        self.stopped = True

    @staticmethod
    def get_devices():
        """Static Function to list the midi devices on this computer"""
        devices = mido.get_ioport_names()
        return devices
        
class TestPort(mido.ports.BaseIOPort):
    """A virtual midi port for testing"""
    def __init__(self, callback=None):
        super(mido.ports.BaseIOPort, self).__init__()
        self.name = "Test Port"
        self.closed = False
        self.callback = callback
        if callback:
            self.callback_thread = Thread(target=self.callback_monitor)
            self.callback_thread.start()

    def random_msg(self):
        msg = None
        r = random.random()
        drums = [
            38,
            48,
            45,
            43
        ]
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
        if r > 0.95:
            msg = random.choice(kit_chng)
        elif r > 0.9:
            msg = random.choice(other)
        else:
            msg = random.choice(notes)
            msg.note = random.choice(drums)
        return msg
    
    def callback_monitor(self):
        """Callback function called when a message is recv"""
        while not self.closed:
            time.sleep(random.random()*0.2)
            msg = self.random_msg()
            print(f"TestPort Send: [{msg}]")
            self.callback(msg)

    def _open(self):
        pass

    def _close(self):
        self.closed = True
        if self.callback is not None:
            self.callback_thread.join()

    def _send(self, msg):
        pass

    def _receive(self, block=False):
        msg = self.random_msg()
        time.sleep(random.random())
        return msg

    
