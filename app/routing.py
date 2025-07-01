from django.urls import re_path
from app.consumers import TeamConsumer, MatchConsumer, PlayerConsumer

websocket_urlpatterns = [
    re_path(r'ws/team/(?P<league_id>\w+)/$', TeamConsumer.as_asgi()),
    re_path(r'ws/matches/(?P<league_id>\w+)/$', MatchConsumer.as_asgi()),
    re_path(r'ws/players/(?P<league_id>\w+)/$', PlayerConsumer.as_asgi()),
]
