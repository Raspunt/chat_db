import asyncio
import json
from tokenize import group
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User

from django.db import IntegrityError

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from . models import Message
from . models import Chat

from . parserNews.News import startUpdateNewsThread
from . parserNews.News import pwdJson
from   additional_func import json_funcs


from WebSocketSender.consumers import ChatConsumer



def get_NewsJson(request):


    if request.method == "POST":

        jsonFile = open(pwdJson,"r")
        data = json.load(jsonFile)


            


        return JsonResponse(data)
    
    return HttpResponse("неужели Это Get запрос? ")



def create_message(request):

    if request.method == "POST" :

        chat_id = request.POST.get("chat_id")
        username = request.POST.get("username")
        text = request.POST.get("text")


        if text == None:
            text = ""

        try:     

            user = User.objects.get(username=username)

            message = Message(autor=user,text=text)
            message.save()


            chat_id_int = int(chat_id) + 1
            current_chat = Chat.objects.get(pk=chat_id_int)
            
            current_chat.messages.add(message)
            
            # оптравляет последнее сообщение обратно
            MesData = {}
            MesData["username"] = username
            MesData["text"] = text

            hour = message.date.hour
            minute = message.date.minute
            MesData["date"] =  f"{hour}:{minute}"

             
            
            JsonData = json.dumps(MesData)  

            group_layer = get_channel_layer()


            async_to_sync(group_layer.group_send)('chat_online', {
            'type': 'events.alarm',
            'content': JsonData
            })


            # ChatConsumer.MessageSended = True
            # ChatConsumer.josnMessage = JsonData




            # channel_layer = get_channel_layer()
            
            # async_to_sync(channel_layer.group_send(
            # "last_message", 
            # {
            #     "type": "send_message",
            #     "message":JsonData
            # }
            # )
            # )




            return HttpResponse(JsonData, content_type="application/json")




        except Chat.DoesNotExist as e:
            return HttpResponse(e)

        except User.DoesNotExist as e:
            return HttpResponse(e)



    elif (request.method == "GET"):
        return HttpResponse("GET запрос")



def create_userPost(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:

            if username != None and password != None:

                User.objects.create_user(username=username,
                    password=password)

                return HttpResponse("Успешный успех")

        except IntegrityError:
            return HttpResponse("user already exsists")


    return HttpResponse("пользователь не создан")



def isUserAutificated(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        if username != "" and password != "":

            if User.objects.filter(username=username).exists():
                
                user = User.objects.get(username=username)

                if user.check_password(password):
                    return HttpResponse("passwordRight")
                else :
                    return HttpResponse("passwordWrong")

               
            else :

                return HttpResponse("UserNotExists")


        else:

             return HttpResponse("DataNotFound")



def get_ChatJson(request):

    if request.method == "POST":
        
        
        chats = Chat.objects.all()
        

        chatsList = []

        for ch in chats:
            DistData = {}
            DistData[f"chat_id"] = ch.id
            DistData[f"chat_title"] = ch.title
            DistData[f"chat_disc"] = ch.disc

            chatsList.append(DistData)

            


        JsonData = json.dumps(chatsList)        

        return HttpResponse(JsonData, content_type="application/json")

    return HttpResponse("я хз")




def Get_MessagesByChat_ID(request):


    if request.method == "POST":

        chat_id_str  = request.POST.get("chat_id")
        chat_id = int(chat_id_str) + 1


        JsonData = json_funcs.GetJsonChatMessagesById(chat_id)        


        return HttpResponse(JsonData, content_type="application/json")





# def startThread(request):

#     startUpdateNewsThread()




