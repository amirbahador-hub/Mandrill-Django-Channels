from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [

    path('', include(('workgenius.socketapp.urls', 'socket'))),
    path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("doc/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('admin/', admin.site.urls),
    path('api/', include(('workgenius.api.urls', 'api'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
