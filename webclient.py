#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import json


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        publish_fmt = {
            "BatteryStatus":"%",
            "CurrentPosition":"m",
            "Velocity":"m/s",
            "Obstacle":["YES", "NO"],
            "Timestamp":0,
            "Sensor":{
                "O2":"%",
                "CO2":"%",
                "Humidity":"%",
                "Temperature":"C"
            }
        }

        publish_data = json.dumps(publish_fmt)
        await websocket.send(publish_data)

        data = await websocket.recv()
        data = json.loads(data)
        print(data)

while True:
    asyncio.get_event_loop().run_until_complete(hello())
    time.sleep(0.5)