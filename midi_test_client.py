#Suppress the hello message from PyGame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from td50x import TD50X
from wled import WledWebsocket
import sys
import random
import mido
import json

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


#Wled websocket
wled = WledWebsocket("ws://192.168.1.199/ws")
wled.start()

colors = ["ff0000", "0dff00"]
notes = {
    TD50X.NoteNumbers.SNARE_HEAD: 0,
    TD50X.NoteNumbers.TOM_1: 0,
    TD50X.NoteNumbers.TOM_2: 0,
}

def msg_recv(msg):
    if msg.type == 'note_on' and msg.note == TD50X.NoteNumbers.SNARE_HEAD.value:
        print("Snare Hit: Sending WLED Message")
        color = colors[notes[TD50X.NoteNumbers.SNARE_HEAD]]
        notes[TD50X.NoteNumbers.SNARE_HEAD] = (notes[TD50X.NoteNumbers.SNARE_HEAD]+1) % 2
        wled.send({"seg": {"id": "0", "i":[0, 10, color]}})
    if msg.type == 'note_on' and msg.note == TD50X.NoteNumbers.TOM_1.value:
        print("Tom 1 Hit: Sending WLED Message")
        color = colors[notes[TD50X.NoteNumbers.TOM_1]]
        notes[TD50X.NoteNumbers.TOM_1] = (notes[TD50X.NoteNumbers.TOM_1]+1) % 2
        wled.send({"seg": {"id": "0", "i":[0, 10, color]}})
    if msg.type == 'note_on' and msg.note == TD50X.NoteNumbers.TOM_2.value:
        print("Tom 2 Hit: Sending WLED Message")
        color = colors[notes[TD50X.NoteNumbers.TOM_2]]
        notes[TD50X.NoteNumbers.TOM_2] = (notes[TD50X.NoteNumbers.TOM_2]+1) % 2
        wled.send({"seg": {"id": "0", "i":[0, 10, color]}})

#Get Midi Devices
devices = TD50X.get_midi_devices()
devices.append("TestPort")

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
td50x = TD50X(devices[selection], msg_callback=msg_recv)
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
        wled.stop()
        wled.join()
        quit(0)
    if len(selection) == 0:
        continue
    if selection[0] == 0:
        if len(selection) >= 2 and selection[1] <= 100 and selection[1] > 0:
            # Set Kit Number
            td50x.set_kit(selection[1])
        else:
            print("To select a kit, enter 0 followed by the kit number [1-100]")
    if selection[0] == 1:
        td50x.refresh_current_kit()
