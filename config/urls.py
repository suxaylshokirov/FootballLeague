from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("authenticate.urls")),
    path("api/v1/app", include("app.urls"))
] +  static(MEDIA_URL, document_root=MEDIA_ROOT)


# Tokens
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]