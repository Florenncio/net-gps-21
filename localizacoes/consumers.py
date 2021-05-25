import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_tosync

from .models import Localizacao

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
    
    async def websocket_receive(self, event):
        print('receive', event)

    async def websocket_discoennect(self, event):
        print('disconnected', event)
    
    
