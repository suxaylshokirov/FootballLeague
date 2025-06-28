from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("authenticate.urls")),
    path("api/v1/app", include("app.urls"))
] +  static(MEDIA_URL, document_root=MEDIA_ROOT)