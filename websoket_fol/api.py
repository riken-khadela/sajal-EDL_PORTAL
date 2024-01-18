import asyncio
import websockets
import time, json
from  bot import Bot

connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    bot_ = Bot()
    bot_.get_local_driver()
    bot_.work()
    try:
        while True:
            # Sending a message to the client every 5 seconds
            message = "Hello from the server!"
            for conn in connected:
                await conn.send(json.dumps(bot_.return_main_data()))
            time.sleep(5)
    finally:
        # Unregister.
        connected.remove(websocket)

start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
