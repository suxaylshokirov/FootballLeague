from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import TeamViewSet, MatchesViewSet

router = DefaultRouter()
router.register('team', TeamViewSet)

matches_router = DefaultRouter()
matches_router.register(r'', MatchesViewSet, basename='matches')

urlpatterns = [
    path('matches/', include(matches_router.urls)),
]

urlpatterns += router.urls
