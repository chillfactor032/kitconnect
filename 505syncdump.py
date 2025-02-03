import sys
from midi_connection import MidiConnection

#Vars
device = None
selection = -1

#Functions
def quit(code):
    print(f"Exit Code:{code}")
    sys.exit(code)

def msg_recv(msg):
    print(msg.dict())

#Get Midi Devices
devices = MidiConnection.get_devices()

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
midi = MidiConnection(devices[selection], msg_recv, None)
midi.start()

try:
    input("Press any key to quit\n")
except KeyboardInterrupt:
    pass

midi.stop()
quit(0)
