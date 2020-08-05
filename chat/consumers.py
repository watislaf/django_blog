import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from django.utils import timezone

import redis
from django.conf import settings
import ast

CHAT_SIZE = 20


class MyMessage:
    message = ''
    user = ''
    datetime = ''

    def __init__(self, message):
        self.message = message

    def to_dict(self, username):
        return {
            'type': 'chat_message',
            'message': self.message,
            'user': username,
            'date': timezone.now().isoformat()
        }


class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data=None, bytes_data=None):
        message = MyMessage(json.loads(text_data)['message'])
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            message.to_dict(self.user.username)
        )
        redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                           port=settings.REDIS_PORT, db=0, decode_responses=True)

        my_list = redis_instance.get('chat_history')
        if my_list == None:
            my_list = ''
        my_list = my_list.split('#')
        my_list.append(message.to_dict(self.user.username).__str__())
        my_list = my_list[:CHAT_SIZE]
        my_list = '#'.join(my_list)

        redis_instance.set('chat_history', my_list)

    def connect(self):
        self.user = self.scope['user']
        self.room_group_name = 'chat'
        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                           port=settings.REDIS_PORT, db=0, decode_responses=True)
        self.accept()
        my_list = redis_instance.get('chat_history')
        if my_list != None:
            for message in my_list.split('#'):
                if message != '':
                    self.chat_message(ast.literal_eval(message))

    # receive message from WebSocket
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
