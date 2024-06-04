import threading
import queue
import logging
import time
import asyncio
import json
import websockets
from PySide6.QtCore import QObject, Signal

class WledWebsocket(threading.Thread):

    class Signals(QObject):
        log = Signal(str)

    def __init__(self, url, **kwargs):
        super().__init__()
        self.url = url
        self._stopped = False
        self.outbox = queue.SimpleQueue()
        self.send_rate_limit_secs = float(kwargs.get("send_rate_limit_secs", 0.001))
        self.last_sent_time = 0
        self._connected = False
        self.signals = self.Signals()

    def log(self, msg):
        self.signals.log.emit(msg)

    def connected(self):
        return self._connected

    def on_message(self, msg):
        #self.log(msg)
        pass

    def stop(self):
        self._stopped = True

    def send(self, msg):
        self.outbox.put(msg)

    async def recv(self, websocket):
        try:
            return await websocket.recv()
        except Exception as e:
            #self.log("Error recv new message")
            #self.log(str(e))
            return None

    async def send_recv(self):
        try:
            websocket_generator = websockets.connect(self.url)
            async for websocket in websocket_generator:
                self.log("WLED Websocket Connection Opened")
                self._connected = True
                try:
                    while not self._stopped:
                        if not self.outbox.empty():
                            if time.time() - self.last_sent_time > self.send_rate_limit_secs:
                                msg = self.outbox.get_nowait()
                                await websocket.send(msg)
                                self.last_sent_time = time.time()
                        try:
                            msg = await asyncio.wait_for(self.recv(websocket), timeout=0.001)
                            self.on_message(msg)
                        except TimeoutError:
                            pass
                        except json.JSONDecodeError as e:
                            self.log("JSON decode error sending a message")
                            self.log(str(e))
                    await websocket.close()
                    self.log("WLED Websocket Connection Closed")
                    break
                except websockets.ConnectionClosed as e:
                    self.log("WLED Websocket Connection closed Unexpectedly")
                    self.log(str(e))
                    continue
        except websockets.exceptions.InvalidURI as e:
            self.log(str(e))
        except OSError as e:
            self.log("OSError: TCP Connection Failed")
            self.log(str(e))
        except websockets.exceptions.InvalidHandshake as e:
            self.log("Websocket Handshake Failed")
            self.log(str(e))
        except Exception as e:
            self.log("Generic Websocket Connection Error")
            self.log(str(e))
        self._connected = False

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.send_recv())
        loop.run_until_complete(loop.shutdown_asyncgens())
        self._connected = False

if __name__ == "__main__":
    pass
