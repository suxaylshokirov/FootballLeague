# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RefereeMatchViewSet

router = DefaultRouter()
router.register(
    r'referee/(?P<referee_id>\d+)/matches',
    RefereeMatchViewSet,
    basename='referee-matches'
)

urlpatterns = [
    path('', include(router.urls)),
]
