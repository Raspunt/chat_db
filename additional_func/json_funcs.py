import json


from MainProg.models import Chat
from MainProg.models import Message




def GetJsonChatMessagesById(chat_id:int):

    

    chat = Chat.objects.get(pk=chat_id)

    mesArr = []


    for mes in chat.messages.all():
        MesData = {}

        MesData["author"] = mes.autor.username
        MesData["text"] = mes.text

        hour = mes.date.hour
        minute = mes.date.minute

        MesData["date"] =  f"{hour}:{minute}"
        mesArr.append(MesData)

    return json.dumps(mesArr)