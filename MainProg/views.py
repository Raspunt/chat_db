import json
import datetime 
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from . models import Message

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


        if username != None and password != None:

            if User.objects.filter(username=username).exists():
                
                user = User.objects.get(username=username)

                if user.check_password(password):
                    return HttpResponse("пароль  правельный ")
                else :
                    return HttpResponse("пароль не правельный")

               
            else :

                return HttpResponse("пользователь не существует")


        else:

             return HttpResponse("нету информации у пользователя")









def startThread(request):

    startUpdateNewsThread()





