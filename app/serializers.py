from rest_framework.serializers import ModelSerializer

from app.models import Team, Match


class TeamModelSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"
