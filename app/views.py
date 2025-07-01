from rest_framework.viewsets import ModelViewSet
from app.models import Team, Match
from app.serializers import TeamModelSerializer, MatchSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamModelSerializer


class MatchesViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
