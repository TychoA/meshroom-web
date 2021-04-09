const websocket = new WebSocket("ws://127.0.0.1:5678");
websocket.onmessage = (event) => {

    console.log(event);
};
