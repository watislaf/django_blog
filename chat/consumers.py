import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data = None, bytes_data = None):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        # send message to WebSocket
        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    def connect(self):
        self.room_group_name = 'chat'
        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    # receive message from WebSocket
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data = json.dumps(event	))
        
