import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TeamConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        league_id = self.scope['url_route']['kwargs'].get("league_id")
        self.group_name = f"league_{league_id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def team_update(self, event):
        print(10)
        # Guruhdagi barcha klientlarga yangilangan ma'lumotni yuborish
        await self.send(text_data=json.dumps({
            'type': 'team_update',
            'data': event['data']
        }))


class MatchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        league_id = self.scope['url_route']['kwargs'].get("league_id")
        self.group_name = f"league_{league_id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def match_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'match_update',
            'data': event['data']
        }))
