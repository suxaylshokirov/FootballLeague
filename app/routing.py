from django.urls import re_path

from app.consumers import TeamConsumer

websocket_urlpatterns = [
    re_path(r'ws/team/(?P<league_id>\w+)/$', TeamConsumer.as_asgi()),
]