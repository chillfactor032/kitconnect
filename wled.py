import threading
import queue
import logging
import time
import asyncio
import json
import websockets

class WledWebsocket(threading.Thread):
    def __init__(self, url, **kwargs):
        super().__init__()
        self.url = url
        self._stopped = False
        self.outbox = queue.SimpleQueue()
        self.send_rate_limit_secs = float(kwargs.get("send_rate_limit_secs", 0.015))
        self.logger = kwargs.get("logger", logging.getLogger(__name__))
        self.last_sent_time = 0

    def on_message(self, msg):
        self.logger.info(msg)

    def stop(self):
        self._stopped = True

    def send_bulk(self, msgs: list, retransmit=False):
        if retransmit:
            msgs.extend(msgs)
        for msg in msgs:
            self.outbox.put(msg)

    def send(self, msg, retransmit=False):
        if retransmit:
            self.outbox.put(msg)
        self.outbox.put(msg)

    async def recv(self, websocket):
        try:
            return await websocket.recv()
        except Exception as e:
            self.logger.error("Error recv new message")
            self.logger.error(e)
            return None

    async def send_recv(self):
        try:
            websocket_generator = websockets.connect(self.url)
            async for websocket in websocket_generator:
                self.logger.info("WLED Websocket Connection Opened")
                try:
                    while not self._stopped:
                        if not self.outbox.empty():
                            if time.time() - self.last_sent_time > self.send_rate_limit_secs:
                                msg = self.outbox.get_nowait()
                                await websocket.send(json.dumps(msg))
                                self.last_sent_time = time.time()
                        try:
                            msg = await asyncio.wait_for(self.recv(websocket), timeout=0.001)
                            self.on_message(msg)
                        except TimeoutError:
                            pass
                        except json.JSONDecodeError as e:
                            self.logger.error("JSON decode error sending a message")
                            self.logger.error(e)
                    await websocket.close()
                    self.logger.info("WLED Websocket Connection Closed")
                    break
                except websockets.ConnectionClosed as e:
                    self.logger.warning(
                        "WLED Websocket Connection closed Unexpectedly")
                    self.logger.debug(e)
                    continue
        except websockets.exceptions.InvalidURI as e:
            self.logger.error(e)
        except OSError as e:
            self.logger.error("OSError: TCP Connection Failed")
            self.logger.error(e)
        except websockets.exceptions.InvalidHandshake as e:
            self.logger.error("Websocket Handshake Failed")
            self.logger.error(e)
        except Exception as e:
            self.logger.error("Generic Websocket Connection Error")
            self.logger.error(e)

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.send_recv())
        loop.run_until_complete(loop.shutdown_asyncgens())


if __name__ == "__main__":
    pass
