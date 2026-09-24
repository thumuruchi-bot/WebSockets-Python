import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    server = await websockets.serve(
        echo,
        "localhost",
        8765
    )

    print("WebSocket Server Started on ws://localhost:8765")

    await server.wait_closed()

asyncio.run(main())
