

from django.urls import path
from . views import get_NewsJson,create_message

urlpatterns = [
    path("get_NewsJson/",get_NewsJson),
    path("create_message/",create_message)
]
