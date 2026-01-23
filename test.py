import asyncio
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription

pcs = set()

async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs.add(pc)
    print("Nueva conexión WebRTC")

    @pc.on("datachannel")
    def on_datachannel(channel):
        print(f"DataChannel creado: {channel.label}")

        # Mensajes desde el navegador
        @channel.on("message")
        def on_message(message):
            print(f"[Browser] {message}")

            # Responder automáticamente (eco)
            if channel.readyState == "open":
                channel.send(f"ECO: {message}")

    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.json_response({
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type
    })

# Middleware CORS para Live Server
@web.middleware
async def cors_middleware(request, handler):
    if request.method == "OPTIONS":
        return web.Response(headers={
            "Access-Control-Allow-Origin": "http://127.0.0.1:5500",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        })
    resp = await handler(request)
    resp.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    return resp

app = web.Application()
app.middlewares.append(cors_middleware)
app.router.add_post("/offer", offer)

print("Servidor Python corriendo en http://localhost:8080")
web.run_app(app, port=8080)
