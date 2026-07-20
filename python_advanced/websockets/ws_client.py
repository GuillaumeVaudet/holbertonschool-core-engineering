#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print(message)
        print("connection closed")

if __name__ == "__main__":
    asyncio.run(hello())
