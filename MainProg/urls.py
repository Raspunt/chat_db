from django.urls import path
from . views import *

urlpatterns = [
    path("get_NewsJson/",get_NewsJson),
    path("get_chatJson/",get_ChatJson),
    path("get_MessagesByChatId/",Get_MessagesByChat_ID),
    path("create_message/",create_message),
    path("create_user/",create_userPost),
    path("IsUserAuthenticated/",isUserAutificated),
    path("Create_Chat/",CreateChatAndReturnThem),
]
