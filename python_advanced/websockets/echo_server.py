#!/usr/bin/env python3

import asyncio
import logging
from websockets.asyncio.server import serve


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)


async def connection_handler(websocket):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(message)
        print("connection closed by the client")


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
