from time import sleep
from fastapi import FastAPI
import socketio
from fastapi.staticfiles import StaticFiles
from fastapi_socketio import SocketManager
from starlette.middleware.cors import CORSMiddleware
import pet_live
import threading
import asyncio
import json

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*'
)

app = FastAPI()
sio_app = socketio.ASGIApp(sio)

origins = ["*, http://localhost:3000, ws://localhost:3000/"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("//static", StaticFiles(directory="panda_emoji"), name="static")
app.mount('/ws', sio_app)

# Принять подключение к сокету
@sio.on
async def connect(sid, environ):
    print("connect ", sid)


# Вернуть index.html
@app.get("/")
async def get_main_page():
    await sio.emit('FromAPI', 80)
    return "Lol"

@app.get("/button")
async def get_button_click(text: str):
    pet_live.panda.panda_eat()
    try:
        await sio.emit('panda_state', json.dumps({'food': pet_live.panda.food, 'happiness': pet_live.panda.happiness, 'health': pet_live.panda.health, 'tired': pet_live.panda.tired, 'age': pet_live.panda.age, 'name': pet_live.panda.name, 'is_alive': pet_live.panda.is_alive, 'is_sleeping': pet_live.panda.is_sleeping, 'is_eating': pet_live.panda.is_eating, 'is_playing': pet_live.panda.is_playing, 'is_sick': pet_live.panda.is_sick, 'is_hungry': pet_live.panda.is_hungry, 'is_tired': pet_live.panda.is_tired, 
        'is_bored': pet_live.panda.is_bored, 'is_happy': pet_live.panda.is_happy, 'is_coocking': pet_live.panda.is_coocking}))
    except Exception as e:
        print(e)
    print(text)

threading.Thread(target=pet_live.panda_live).start()

async def send_panda_state():
    while True:
        print(pet_live.panda)
        try:
            await sio.emit('panda_state', json.dumps({'food': pet_live.panda.food, 'happiness': pet_live.panda.happiness, 'health': pet_live.panda.health, 'tired': pet_live.panda.tired, 'age': pet_live.panda.age, 'name': pet_live.panda.name, 'is_alive': pet_live.panda.is_alive, 'is_sleeping': pet_live.panda.is_sleeping, 'is_eating': pet_live.panda.is_eating, 'is_playing': pet_live.panda.is_playing, 'is_sick': pet_live.panda.is_sick, 'is_hungry': pet_live.panda.is_hungry, 'is_tired': pet_live.panda.is_tired, 
            'is_bored': pet_live.panda.is_bored, 'is_happy': pet_live.panda.is_happy, 'is_coocking': pet_live.panda.is_coocking}))
        except Exception as e:
            print(e)
        sleep(2)

threading.Thread(target=asyncio.run, args=(send_panda_state(),)).start()