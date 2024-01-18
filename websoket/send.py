import asyncio, random
import websockets, time, json
from bot import Bot

async def send_data():
    uri = "ws://localhost:8765"  # Update with your WebSocket server details

    async with websockets.connect(uri) as websocket:
        bot_ = Bot()
        bot_.get_local_driver()
        bot_.work()
        
        while True:
            data_to_send = bot_.return_main_data()
            await websocket.send(data_to_send)
            print(f"Sent data: {data_to_send}")
            time.sleep(random.randint(5,10)/10)
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_data())
