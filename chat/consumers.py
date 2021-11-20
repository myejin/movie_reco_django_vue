import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # 그룹이름은 영문자, 숫자, 하이픈, 마침표만 가능하다.
        self.room_group_name = "chat_%s" % self.room_name

        # 룸그룹에 가입합니다.
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        # 웹소켓 연결 수락
        # 연결 수락 전 권한을 체크할 수 있다.
        await self.accept()

    async def disconnect(self, close_code):
        # group_discard : 그룹을 탈퇴합니다.
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # group_send : 그룹에 이벤트를 보냅니다.
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # 웹소켓에 메세지를 보낸다.
        await self.send(text_data=json.dumps({"message": message}))
