from django.urls import path

from app.views import PlayerLeagueTableListApiView, player_list_view

urlpatterns = [
    path('player/league/table', PlayerLeagueTableListApiView.as_view()),
    path('players/live/', player_list_view),
]
