import json
import wave
import asyncio
import websockets

stop = False


async def send_audio(ws, audio_path):
    global stop

    wf = wave.open(audio_path, 'rb')
    buffer_size = int(wf.getframerate() * 0.1)
    while True:
        data = wf.readframes(buffer_size)
        if len(data) == 0:
            stop = True
            break
        await ws.send(data)
        await asyncio.sleep(0.05)


async def receive_messages(ws):
    while not stop:
        try:
            message = await ws.recv()
            print(f"Received message: {json.loads(message)}")
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break


async def run_test():
    url = 'wss://jppoc.namisense.ai/connect?sample_rate=16000'
    audio_path = 'audio_jp.wav'

    async with websockets.connect(url) as ws:
        await asyncio.gather(send_audio(ws, audio_path), receive_messages(ws))


if __name__ == '__main__':
    asyncio.run(run_test())
