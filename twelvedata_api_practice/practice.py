import asyncio
import csv
import json
import os
import websockets
import env as e

TWELVE_API_KEY = os.getenv("TWELVE_API_KEY", None)


url = f"wss://ws.twelvedata.com/v1/quotes/price?apikey={TWELVE_API_KEY}"


async def run():
    _ws = await websockets.connect(url, ping_interval=10,)
    await _ws.send(json.dumps(e.PARAMS))
    await _ws.send(json.dumps(e.PARAMS2))
    with open('histories.csv', 'a') as file:
        writer = csv.writer(file)

        while True:
            message = await _ws.recv()
            data = json.loads(message)
            writer.writerow(data.keys())
            writer.writerow(data.values())
            print(data)

if __name__ == "__main__":
    asyncio.run(run())
