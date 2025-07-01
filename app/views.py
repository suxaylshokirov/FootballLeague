from rest_framework.generics import ListAPIView
from django.shortcuts import render
from app.models import Player
from app.serializers import PlayerLeagueTableModelSerializer


class PlayerLeagueTableListApiView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerLeagueTableModelSerializer


def player_list_view(request):
    return render(request, 'player_list.html')