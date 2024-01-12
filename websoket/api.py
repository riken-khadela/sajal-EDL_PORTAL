import asyncio
import websockets,json

async def handle_websocket_connection(websocket, path):
    try:
        while True:
            # Receive data from the client
            print(1)
            data = await websocket.recv()

            if data is None:
                break

            print(f"Received data: {json.loads(data)}")

            # Process the json.loads(data) or perform any required tasks

            # Send a response back to the client (if needed)
            await websocket.send(f"Server received: {json.loads(data)}")

    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket connection closed successfully.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed unexpectedly: {e}")

if __name__ == "__main__":
    # Run the WebSocket server
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(handle_websocket_connection, "localhost", 8765,ping_interval=None)
    )
    asyncio.get_event_loop().run_forever()
