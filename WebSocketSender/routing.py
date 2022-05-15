
from django.urls import path
from . consumers import ChatConsumer

ws_urlpatterns = [
    path("JsonData",ChatConsumer.as_asgi())
]