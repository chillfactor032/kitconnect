#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from td50x import TD50X
import sys
import random

#Some Test Msgs
test_msgs = [
    [0xC9, random.randint(0,127), 0x00, 0x7f],
    [0x93, random.choice(list(TD50X.NoteNumbers)).value, random.randint(1,127), 0x00],
    [0xC6, random.randint(0,127), 0x00, 0x7f]
]

#Vars
device = None
selection = -1
incoming_msg_buffer = []

#Prepared Midi Messages
msgs = [
    {
        "desc": "Program Change Kit 100",
        "msg": [0xC9, 99, 0x00, 0x7F]
    },
    {
        "desc": "Program Change Kit 30",
        "msg": [0xC9, 29, 0x00, 0x7F]
    }
]

#Functions
def quit(code):
    print(f"Exit Code:{code}")
    sys.exit(code)

def recv(msg, timestamp):
    msg = TD50X.to_str(msg)
    print("< "+ msg + f" {timestamp}")

#Get Midi Devices
devices = TD50X.get_midi_devices()

#Select Midi Device
while device is None:
    #Get Devices
    for x in range(len(devices)):
        print(f"[{x}] {devices[x]['desc']}")

    #print options
    try:
        selection = int(input("Select a Midi Device:"))
        print()
    except ValueError as ve:
        print("Invalid Answer. Make it an integer please.")
        continue
    except KeyboardInterrupt as ke:
        print("\nKeyboard Interrupt. Goodbye.")
        quit(0)
    print(f"You selected [{selection}] {devices[selection]['name']}\n")
    device = devices[selection]

#Create MidiConnection
td50x = TD50X(device["input_id"],device["output_id"])
td50x.midi.test_msgs = test_msgs
td50x.midi_start(test=True)

#Send / Recv Midi Packets
while True:
    #print options
    i = 0
    print("----------------------")
    for i in range(len(msgs)):
        option = msgs[i]
        print(f"[{i}] {option['desc']}")
    print("----------------------")
    try:
        selection = int(input("Make Selection:\n"))
    except ValueError as ve:
        continue
    except KeyboardInterrupt as ke:
        print("\nKeyboard Interrupt.")
        td50x.midi_stop(wait=True)
        quit(0)
    if selection >= 0 and selection < len(msgs):
        td50x.send_msg(msgs[selection]["msg"])
    else:
        print("Bad selection try again.")
