from rest_framework.serializers import ModelSerializer

from app.models import Team


class TeamModelSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"