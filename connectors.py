import threading
import queue
import logging
import time
import asyncio
import json
import websockets
import socket
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

class UdpClient(threading.Thread):

    class Signals(QObject):
        log = Signal(str)

    def __init__(self, host, port, **kwargs):
        super().__init__()
        self.host = host
        self.port = port
        self._stopped = False
        self.outbox = queue.SimpleQueue()
        self.signals = self.Signals()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = ""
        
    def set_host(self, host:str, port:int):
        self.host = host
        self.port = port
        self.ip = ""
        self.log(f"UDP Client: Setting Host [{self.host}:{self.port}]")
        try:
            info = socket.getaddrinfo(self.host, self.port, proto=socket.AF_INET)
        except socket.gaierror as e:
            self.log(f"Error setting UDP Address [{self.host}:{self.port}]")
            self.log(e)
            return False
        if len(info) > 0:
            self.info = info[0]
            self.ip = self.info[4][0]
            return True
        return False

    def stop(self):
        self._stopped = True

    def send(self, msg):
        self.outbox.put(msg)

    def run(self):
        self.log("UDP Client Starting")
        if self.ip == "":
            self.set_host(self.host, self.port)
        while not self._stopped:
            if not self.outbox.empty():
                msg = self.outbox.get_nowait()
                try:
                    self.socket.sendto(msg.encode(), (self.host, self.port))
                except socket.gaierror:
                    pass
        self.log("UDP Client Stopped")

    def log(self, msg):
        self.signals.log.emit(msg)

if __name__ == "__main__":
    pass
