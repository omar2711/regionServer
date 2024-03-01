# serverapi/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComputerViewSet

# Crear un router y registrar nuestros viewsets con él.
router = DefaultRouter()
router.register(r'computers', ComputerViewSet)

# Las URLs de la API son ahora determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]
