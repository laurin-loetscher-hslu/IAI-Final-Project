from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Store all connected clients
connected_clients: List[WebSocket] = []


@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(data)
    except WebSocketDisconnect:
        if websocket in connected_clients:
            connected_clients.remove(websocket)
