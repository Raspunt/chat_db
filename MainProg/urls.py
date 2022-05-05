from django.urls import path
from . views import get_NewsJson,create_message,create_userPost

urlpatterns = [
    path("get_NewsJson/",get_NewsJson),
    path("create_message/",create_message),
    path("create_user/",create_userPost)
]
