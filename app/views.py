# Include our application
from app import app
from flask import render_template
import asyncio
import websockets

# Define a route which will capture all routes and link them back to index
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def index(path):

    # Return the index page. By default, Flask will look into a /templates folder
    return render_template('index.html')

async def hello(websocket, path):
    name = await websocket.recv()
    print(name)

    await websocket.send("hello world " + name)

start_server = websockets.serve(hello, "127.0.0.1", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
