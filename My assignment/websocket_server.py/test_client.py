import asyncio
import websockets
import json

async def test_echo(websocket):
    await websocket.send(json.dumps({"action": "echo", "message": " The quick brown fox jumped over the lazy dog o"}))
    async for message in websocket:
        data = json.loads(message)
        if data["type"] == "echo":
            print("Echo:", data["content"])
        else:
            break

async def test_reverse(websocket):
    await websocket.send(json.dumps({"action": "reverse", "message": " The quick brown fox jumped over the lazy dog o"}))
    async for message in websocket:
        data = json.loads(message)
        if data["type"] == "reverse":
            print("Reverse:", data["content"])
        else:
            break

async def test_count(websocket):
    await websocket.send(json.dumps({"action": "count", "message": " The quick brown fox jumped over the lazy dog o"}))
    message = await websocket.recv()
    data = json.loads(message)
    print("Count:", data["content"])

async def test():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Testing Echo:")
        await test_echo(websocket)
        print("\nTesting Reverse:")
        await test_reverse(websocket)
        print("\nTesting Count:")
        await test_count(websocket)

asyncio.get_event_loop().run_until_complete(test())
