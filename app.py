# Include our application
from app import app
import asyncio
import websockets

async def hello(websocket, path):
    print('websocket')
    while True:
        await websocket.send("hello world")
        await asyncio.sleep(1)

async def ws():
    await websockets.serve(hello, "127.0.0.1", 5678)

async def client():
    app.run()

async def main():
    await asyncio.gather(ws(), client())

asyncio.run(main())
