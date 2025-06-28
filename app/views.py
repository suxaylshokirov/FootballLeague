from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app.models import Team
from app.serializers import TeamModelSerializer


# Create your views here.


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamModelSerializer

