import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomId = self.scope['url_route']['kwargs']['roomId']  # Get sender from URL
        print(self.roomId,"--------------------------------------")
        # Create a unique group for the P2P chat, for example: chat_sender_receiver
        self.room_group_name = f'chat_{self.roomId}'

        # Join the P2P chat group (both sender and receiver will join this group)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()  # Accept the WebSocket connection

    async def disconnect(self, close_code):
        # Leave P2P chat group when disconnected
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket (text_data will be in JSON format)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        senderId = text_data_json.get('senderId')  # Use sender from the WebSocket if not provided

        # Send message to the P2P group (this sends to the receiver only)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',  # This is the custom event type to send the message
                'message': {'text': message, 'senderId': senderId}
            }
        )

    async def chat_message(self, event):
        # Send the message to WebSocket client
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
