from django.urls import path

from app.views import PlayerLeagueTableListApiView, PlayerCreateApiView

urlpatterns = [
    path('player/league/table', PlayerLeagueTableListApiView.as_view()),
    path('player/create/', PlayerCreateApiView.as_view())
]
