# app/views.py
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from app.models import Match
from app.serializers import MatchSerializer

@extend_schema(tags=['Referee'])
class RefereeMatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        referee_id = self.kwargs.get('referee_id')
        return Match.objects.filter(referee__id=referee_id)

    def perform_create(self, serializer):
        referee_id = self.kwargs.get('referee_id')
        serializer.save(referee_id=referee_id)
