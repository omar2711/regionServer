# serverapi/routing.py
from django.urls import path
from .consumers import ComputerInfoConsumer

websocket_urlpatterns = [
    path('ws/computer/', ComputerInfoConsumer.as_asgi()),
]
