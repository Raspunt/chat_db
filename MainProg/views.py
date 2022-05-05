import json
import datetime 
from django.shortcuts import render
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
        print(request.POST,"it was here")

        username = request.POST.get("username")
        text = request.POST.get("text")

        if User.objects.filter(username=username).exists() :
            print("User exists")

            user = User.objects.get(username=username)

            print(user)

            message = Message(autor=user,text=text)
            message.save()



        else :
            print("net")
            # User.objects.create_user(username,"mail@ru","password1")


    return HttpResponse("сообщение готово")



def startThread(request):

    startUpdateNewsThread()





