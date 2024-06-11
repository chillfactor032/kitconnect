from pynput import keyboard
from connectors import UdpClient
import json

client = UdpClient("wled-sinise.local", 21324)
client.start()

def on_press(key):
    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        num = key.vk - 96
        if num == 0:
            msg = {'flash': {'seg': [0,1,2,3], "choke": 1}}
        else:
            msg = {'flash': {'seg': [num-1], "dur": 1500}}
        print(msg)
        client.send(json.dumps(msg))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()

client.stop()
client.join()
