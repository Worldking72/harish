import asyncio
import websockets
import json
import time

async def echo_message(websocket, message):
    for char in message:
        await websocket.send(json.dumps({"type": "echo", "content": char}))
        await asyncio.sleep(0.1)
    await websocket.send(json.dumps({"type": "echo", "content": "\n"}))  # End of message

async def reverse_message(websocket, message):
    reversed_message = message[::-1]
    for char in reversed_message:
        await websocket.send(json.dumps({"type": "reverse", "content": char}))
        await asyncio.sleep(0.1)
    await websocket.send(json.dumps({"type": "reverse", "content": "\n"}))  # End of message

async def count_last_character(websocket, message):
    if not message:
        count = 0
    else:
        last_char = message[-1]
        count = message[:-1].count(last_char)
    await websocket.send(json.dumps({"type": "count", "content": count}))

async def handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        action = data.get("action")
        content = data.get("message")
        
        if action == "echo":
            await echo_message(websocket, content)
        elif action == "reverse":
            await reverse_message(websocket, content)
        elif action == "count":
            await count_last_character(websocket, content)

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()