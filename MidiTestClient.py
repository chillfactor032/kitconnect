#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from td50x import TD50X
import sys
import random
import mido

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
        "desc": "Set Kit {Kit Num}",
        "msg": ""
    },
    {
        "desc": "Fetch Current Kit",
        "msg": ""
    }
]

#Functions
def quit(code):
    print(f"Exit Code:{code}")
    sys.exit(code)

def recv(msg):
    print(f"< [{msg}]")

#Get Midi Devices
devices = TD50X.get_midi_devices()

#Select Midi Device
while device is None:
    #Get Devices
    for x in range(len(devices)):
        print(f"[{x}] {devices[x]}")

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
    print(f"You selected [{selection}] {devices[selection]}\n")
    device = devices[selection]

#Create MidiConnection
td50x = TD50X(devices[selection])
td50x.midi_start()

#Send / Recv Midi Packets
selection = ""
while True:
    #print options
    i = 0
    print("----------------------")
    for i in range(len(msgs)):
        option = msgs[i]
        print(f"[{i}] {option['desc']}")
    print("----------------------")
    try:
        selection = [int(x) for x in input("Make Selection:\n").split()]
    except ValueError as ve:
        print("Invalid Input: Must be integers")
        continue
    except KeyboardInterrupt as ke:
        print("\nKeyboard Interrupt.")
        print("Waiting for MidiConnection to stop...", end="")
        td50x.midi_stop()
        quit(0)
    if len(selection) == 0:
        continue
    if selection[0] == 0:
        if len(selection) >= 2 and selection[1] <= 100 and selection[1] > 0:
            # Set Kit Number
            td50x.set_kit(selection[1])
        else:
            print("To select a kit, enter 0 followed by the kit number [1-128]")
    if selection[0] == 1:
        td50x.refresh_current_kit()
