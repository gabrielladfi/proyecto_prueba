from django.contrib import admin
from django.urls import path
from django.urls import path
from rest_framework.permissions import AllowAny
from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentación de la API usando Swagger y DRF",
        contact=openapi.Contact(email="contacto@tuapp.com"),
        license=openapi.License(name="BSD License"),
        
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('login/', include('login.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Opcional: interfaz Redoc
]