# Include our application
import asyncio
import websockets
import json
from app.lib.meshroom import Meshroom

async def consumer(websocket, message):
    """
    Consumer callback called when the websocket server receives a message.
    It is expected that every message is a JSON string.
    """
    message = json.loads(message)

    # Handle a run request, at which we want to start a new meshroom process
    if (message['type'] == 'run'):

        # Set up a new meshroom process
        m = Meshroom('tests\input', 'tests\output')
        await m.run('tests\config.json', pipe=websocket)

async def consumer_handler(websocket, path):
    """Handler that installs a callback for when the websocket server receives a message"""
    async for message in websocket:
        await consumer(websocket, message)

# Define the ip address and port at which to run the websocket server
ip = '127.0.0.1'
port = 5678

# Run the websocket server at the designated ip address and port
print(f"starting websocket server at {ip}:{port}")
server = websockets.serve(consumer_handler, ip, port)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()