import asyncio
import pytest
import websockets
from fastapi.testclient import TestClient
import os


# Import the app and connected_clients from the backend package
from backend.chat_server import app, connected_clients

from dotenv import load_dotenv
load_dotenv()

# Create a test client
client = TestClient(app)

@pytest.mark.asyncio
async def test_websocket_message_transmission():
    """
    Test that a message sent through WebSocket is broadcast to all clients
    """
    # Create multiple WebSocket connections
    WEBSOCKET_URI = os.getenv("WEBSOCKET_URI")
    #WEBSOCKET_URI = "ws://localhost:8000/chat"
    async def create_client():
        return await websockets.connect(WEBSOCKET_URI)

    # Create 3 client connections
    clients = [await create_client() for _ in range(3)]

    try:
        # Send a message from the first client
        test_message = "Hello, WebSocket!"
        await clients[0].send(test_message)

        # Check if other clients receive the message
        received_messages = []
        async def receive_message(client):
            try:
                msg = await client.recv()
                received_messages.append(msg)
            except Exception:
                pass

        # Create tasks to receive messages
        receive_tasks = [receive_message(client) for client in clients[1:]]
        await asyncio.gather(*receive_tasks)

        # Assert that all other clients received the message
        assert len(received_messages) == 2
        assert all(msg == test_message for msg in received_messages)

    finally:
        # Close all client connections
        for client in clients:
            await client.close()


@pytest.mark.asyncio
async def test_websocket_connection():
    """
    Test WebSocket connection and ensure it is functional.
    """
    #WEBSOCKET_URI = "ws://localhost:8000/chat"
    WEBSOCKET_URI = os.getenv("WEBSOCKET_URI")

    # Connect to the WebSocket server
    async with websockets.connect(WEBSOCKET_URI) as websocket:
        # Send a simple message to verify the connection
        test_message = "Hello, this is a test!"
        await websocket.send(test_message)

        # Receive the echoed message (if the server is set up for this)
        response = await websocket.recv()

        # Assert that the server echoes the message correctly
        assert response == test_message, f"Expected {test_message}, but got {response}"


@pytest.mark.asyncio
async def test_disconnect_handling():
    """
    Test that the server properly handles WebSocket client disconnection.
    """
    # WEBSOCKET_URI = "ws://localhost:8000/chat"
    WEBSOCKET_URI = os.getenv("WEBSOCKET_URI")

    # Step 1: Connect to the WebSocket server
    async with websockets.connect(WEBSOCKET_URI) as websocket:
        # Verify the connection was established
        initial_message = "Testing disconnection handling"
        await websocket.send(initial_message)
        response = await websocket.recv()
        assert response == initial_message, "Server did not echo the initial message"

        # At this point, the connection should be active.

    # Step 2: The `async with` block ends here, closing the WebSocket connection.
    # After the above block, the client disconnects.

    # Step 3: Verify that the server handled the disconnection
    # In a real implementation, you might check the server's state through logs,
    # a status endpoint, or by reconnecting with another client to confirm the previous client was removed.
    async with websockets.connect(WEBSOCKET_URI) as websocket2:
        # Send a "status check" or similar message
        await websocket2.send("Check connected clients")
        status_response = await websocket2.recv()

        # Verify that the first client is no longer in the list of active connections
        # (This assumes your server can provide such status information)
        assert "client1" not in status_response, "Server did not properly handle disconnect"
