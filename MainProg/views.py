import json
import datetime 
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User


from . models import Message
from . models import Chat

from . parserNews.News import startUpdateNewsThread
from . parserNews.News import pwdJson




def get_NewsJson(request):


    if request.method == "POST":

        jsonFile = open(pwdJson,"r")
        data = json.load(jsonFile)


            


        return JsonResponse(data)
    
    return HttpResponse("неужели Это Get запрос? ")



def create_message(request):

    if request.method == "POST" :
        print(request.POST,f"\n{request.COOKIES}")

        username = request.POST.get("username")
        text = request.POST.get("text")

        if username == "" and text == "":    
            return HttpResponse("параменты username,text пустые ")



        if User.objects.filter(username=username).exists() :
            print("User exists")

            user = User.objects.get(username=username)

            print(user)

            message = Message(autor=user,text=text)
            message.save()

            return HttpResponse("сообщение готово")



        else :
            
            
            return HttpResponse(f"создать пользователя? \nusername {username} ")

    elif (request.method == "GET"):
        return HttpResponse("GET запрос")



def create_userPost(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username != None and password != None:

            User.objects.create_user(username=username,
                password=password)

            return HttpResponse("Успешный успех")

    return HttpResponse("прошел запрос")



def isUserAutificated(request):

    if request.method == "POST":

        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")


        if username != "" and password != "":

            if User.objects.filter(username=username).exists():
                
                user = User.objects.get(username=username)

                if user.check_password(password):
                    print("пароль правильный")
                    return HttpResponse("passwordRight")
                else :
                    print("пароль не правильный")
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

            

            # for mes in ch.messages.all():
            #     mesArr.append(f"{mes.id} {mes.autor} {mes.text}")

            # DistData["messages"] = mesArr

        JsonData = json.dumps(chatsList)        

        return HttpResponse(JsonData, content_type="application/json")

    return HttpResponse("я хз")




def get_messagesByChat_ID(request):


    if request.method == "POST":
        chat = Chat.objects.all()

        mesArr = []


        for mes in chat.messages.all():
            MesData = {}

            MesData["author"] = mes.autor
            MesData["text"] = mes.text
            mesArr.append(MesData)

        
        JsonData = json.dumps(chatsList)        


        return HttpResponse(JsonData, content_type="application/json")



def startThread(request):

    startUpdateNewsThread()




