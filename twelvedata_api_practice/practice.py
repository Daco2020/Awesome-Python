import asyncio
import csv
import json
import websockets
import env as e


async def run():
    _ws = await websockets.connect(e.url, ping_interval=10)
    await _ws.send(json.dumps(e.PARAMS1))
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
