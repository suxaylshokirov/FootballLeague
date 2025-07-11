# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("authenticate.urls")),
    path("api/v1/app/", include("app.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    # OpenAPI schema (JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI (interactive docs)
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc (optional)
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
