const websocket = new WebSocket("ws://127.0.0.1:8765");
ws.onmessage = (event) => {

    console.log(event);
};
