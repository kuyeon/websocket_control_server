#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json

async def web_server(websocket, path):
    publish_fmt = { 
        "Mode": ["Auto", "Manual"],
        "Homing": ["YES", "NO"],
        "STOP": ["YES", "NO"],
        "TargetPosition": "m",
        "Velocity": "m/s",
        "Lamp": ["YES", "NO"],
        "Buzzer": ["YES", "NO"],
        "Timestamp":0
    }

    publish_data = json.dumps(publish_fmt)
    await websocket.send(publish_data)

    data = await websocket.recv()
    data = json.loads(data)
    print(data)


start_server = websockets.serve(web_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


