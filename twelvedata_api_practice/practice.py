import asyncio
import csv
import json
import websockets
import os

from dotenv import load_dotenv


async def run():
    _ws = await websockets.connect(a, ping_interval=10)
    await _ws.send(json.dumps({"action": "subscribe", "params": TWELVEDATA_SYMBOLS}))

    with open("histories.csv", "a") as file:
        writer = csv.writer(file)

        while True:
            message = await _ws.recv()
            data = json.loads(message)
            writer.writerow(data.keys())
            writer.writerow(data.values())
            print(data)


if __name__ == "__main__":
    asyncio.run(run())
