from rest_framework.serializers import ModelSerializer

from app.models import Player


class PlayerLeagueTableModelSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"