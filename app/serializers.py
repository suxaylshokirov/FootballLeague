# app/serializers.py
from rest_framework import serializers
from app.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
