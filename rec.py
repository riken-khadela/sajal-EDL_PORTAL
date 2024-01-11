import asyncio
import websockets

async def handle_client(websocket, path):
    print(f"Client connected from {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            # Process the message or perform actions based on your application's logic
            await websocket.send(f"Received: {message}")
    finally:
        # Close the connection when the client disconnects
        await websocket.close()

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
