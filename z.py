#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8001") as websocket:
        breakpoint()
        websocket.send("Hello a fasef aewfworld! 1111sf wsefg asefge asaaa")
        message = websocket.recv()
        print(f"Received: {message}")

hello()