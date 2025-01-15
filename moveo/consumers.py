from channels.generic.websocket import AsyncWebsocketConsumer
import json

connected_users = {}

first_mentor = {}

class CodeBlockConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer to manage real-time collaboration and user interactions
    within a CodeBlock room.
    """

    async def connect(self):
        """
        Handles a new WebSocket connection.
        - Adds the user to the room's group.
        - Tracks the number of connected users.
        - Identifies the first mentor in the room.
        """
        self.id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = f"codeblock_{self.id}"

        if self.room_group_name not in connected_users:
            connected_users[self.room_group_name] = 0
        connected_users[self.room_group_name] += 1

        if connected_users[self.room_group_name] == 1:
            first_mentor[self.room_group_name] = self.channel_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_count_update',
                'message': f"Current users: {connected_users[self.room_group_name]}"
            }
        )

        if connected_users[self.room_group_name] == 1:
            await self.send(text_data=json.dumps({
                "type": "is_mentor",
            }))

    async def disconnect(self, close_code):
        """
        Handles a WebSocket disconnection.
        - Updates the user count for the room.
        - Handles mentor reassignment if the mentor disconnects.
        - Removes the user from the room's group.
        """

        if self.room_group_name in connected_users:
            connected_users[self.room_group_name] -= 1
            if connected_users[self.room_group_name] == 0:
                del connected_users[self.room_group_name]

        if self.room_group_name in first_mentor and first_mentor[self.room_group_name] == self.channel_name:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'redirect_to_home',
                    'url': '/home'
                }
            )
            del first_mentor[self.room_group_name]

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_count_update',
                'message': f"Current users: {connected_users.get(self.room_group_name, 0)}"
            }
        )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def redirect_to_home(self, event):
        """
        Handles the 'redirect_to_home' message type.
        Sends a redirection URL to the WebSocket client.
        """
        await self.send(text_data=json.dumps({
            'type': 'redirect',
            'url': event['url']
        }))

    async def user_count_update(self, event):
        """
        Handles the 'user_count_update' message type.
        Sends the updated user count to the WebSocket client.
        """
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))

    async def receive(self, text_data):
        """
        Handles incoming WebSocket messages.
        - Parses the incoming data.
        - Broadcasts a 'code_update' message to the group.
        """
        data = json.loads(text_data)
        code = data.get('code', '')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'code_update',  
                'code': code
            }
        )

    async def code_update(self, event):
        """
        Handles the 'code_update' message type.
        Sends the updated code to all WebSocket clients in the group.
        """
        code = event['code']

        await self.send(text_data=json.dumps({
            'type': 'code_update',
            'code': code
        }))
