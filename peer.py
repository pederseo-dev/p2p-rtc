import asyncio
import json
import websockets
from aiortc import RTCPeerConnection, RTCSessionDescription

pc = RTCPeerConnection()
channel = None

@pc.on("datachannel")
def on_datachannel(ch):
    global channel
    channel = ch
    print("DataChannel abierto")

    @ch.on("message")
    def on_message(msg):
        print("[HTML]", msg)

@pc.on("icecandidate")
async def on_icecandidate(c):
    if c:
        await ws.send(json.dumps({"ice": c.toJSON()}))

async def main():
    global ws
    ws = await websockets.connect("ws://localhost:8765")

    async for msg in ws:
        data = json.loads(msg)

        if "sdp" in data:
            sdp = RTCSessionDescription(**data["sdp"])
            await pc.setRemoteDescription(sdp)
            if sdp.type == "offer":
                answer = await pc.createAnswer()
                await pc.setLocalDescription(answer)
                await ws.send(json.dumps({"sdp": {
                    "type": pc.localDescription.type,
                    "sdp": pc.localDescription.sdp
                }}))

        if "ice" in data:
            await pc.addIceCandidate(data["ice"])

asyncio.run(main())
