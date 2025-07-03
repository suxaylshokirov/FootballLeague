from rest_framework.generics import ListAPIView, CreateAPIView
from django.shortcuts import render
from app.models import Player
from app.serializers import PlayerLeagueTableModelSerializer


class PlayerLeagueTableListApiView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerLeagueTableModelSerializer


class PlayerCreateApiView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerLeagueTableModelSerializer