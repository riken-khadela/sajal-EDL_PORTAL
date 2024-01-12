import asyncio, random
import websockets, time, json

class Bot():
    
    def get_data(self) :
        data = {
            "leistuning" : {
                "L1" : f"{random.randint(5,30)}.{random.randint(5,30)} kw",
                "L2" : f"{random.randint(5,30)}.{random.randint(5,30)} kw",
                "L3" : f"{random.randint(5,30)}.{random.randint(5,30)} kw"
                },
            "main" : {
                "L1" : f"{random.randint(5,30)}.{random.randint(5,30)} kw",
                "L2" : f"{random.randint(5,30)}.{random.randint(5,30)} kw",
                "L3" : f"{random.randint(5,30)}.{random.randint(5,30)} kw"
                }
        }
        
        return json.dumps(data)
async def send_data():
    uri = "ws://localhost:8765"  # Update with your WebSocket server details

    async with websockets.connect(uri) as websocket:
        bot_ = Bot()
        while True:
            data_to_send = bot_.get_data()
            await websocket.send(data_to_send)
            print(f"Sent data: {data_to_send}")
            time.sleep(random.randint(5,10)/10)
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_data())
