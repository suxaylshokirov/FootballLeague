from django.urls import path
from rest_framework.routers import DefaultRouter

from app.views import TeamViewSet

router = DefaultRouter()
router.register('team' , TeamViewSet)


urlpatterns = [
]

urlpatterns += router.urls