from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import UsuarioViewSet, IngresoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'ingresos', IngresoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
