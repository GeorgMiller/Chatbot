import time, logging
from datetime import datetime
import threading, collections, queue, os, os.path
import deepspeech
import numpy as np
import pyaudio
import wave
import webrtcvad
from halo import Halo
from scipy import signal
from argparse import Namespace

import argparse
import os

from TTS.server.synthesizer import Synthesizer
import librosa
import librosa.display

from socketio import AsyncClient
import asyncio
from json import dumps
from aioconsole import ainput
import uuid

import IPython
from IPython.display import Audio



synthesizer = None

from utils.audio import AudioProcessor

import torch


sio = AsyncClient()
FullIp = 'http://localhost:5005'

async def connectToServer():
    await sio.connect(FullIp)
    await sio.emit('session_request', {'session_id':'9b91ffa335d244b7978292ae9f17de2e'})
    await sio.emit('user_uttered', {'sender': "nothing", 'message': 'Hello', 'session_id':'9b91ffa335d244b7978292ae9f17de2e'})
    print('connected')
    await sio.wait()


@sio.on('bot_uttered')
async def handle_bot_message(sid):
    await sio.sleep(1)
    data = 'Hello again'
    print(sid)
    await sio.emit('user_uttered', {'sender': "nothing", 'message': data, 'session_id':'9b91ffa335d244b7978292ae9f17de2e'})
    print('Client sent something')

asyncio.run(connectToServer())

