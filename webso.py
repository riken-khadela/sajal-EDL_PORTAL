import asyncio
import websockets

async def connect_to_websocket():
    uri = "wss://echo.websocket.org"  # Replace with your WebSocket URL
    async with websockets.connect(uri) as websocket:
        message = "Hello, WebSocket!"
        print(f"Sending: {message}")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(connect_to_websocket())
