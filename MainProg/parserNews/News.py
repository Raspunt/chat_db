import requests
from bs4 import BeautifulSoup
import json
import os
from threading import Thread
from threading import Event



data_site = {"metalica":[],"AcDc":[]}
pwdJson = os.path.dirname(os.path.realpath(__file__)) + "/json_data.json"


def UpdateJsonData():
    
    while True:
        ParceSite()
        Event().wait(3600)



    


def startUpdateNewsThread():
    process = Thread(target=UpdateJsonData, args=[])
    process.start()

    

def ParceSite():

    urls = [
        "https://www.metallica.com/blog/news/",
        "https://www.acdc.com/news/",
        ]

    data_site = MetalicaParser(urls[0])
    data_site = AcDcParser(urls[1])




    SaveToJson(data_site)
    # print("complete parser")


def MetalicaParser(url):
    # print("request to metalica")
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")



    imgag = soup.find_all("img",{"class":"js-blazy"})
    

    count_i = 0
    for content_data in soup.find_all("div",{"class":"content-info"}):
        count_i = count_i + 1
        title = content_data.find("a").text
        date = content_data.find("h6").text
        text = content_data.find("div",{"class":"content-body__excerpt"}).text

        title = title.replace("\n","")
        date  = date.replace("\n","")
        text  = text.replace("\n","")
    
        data_site["metalica"].append(
            {
                "title":title,
                "date":date,
                "text":text,
                "img":imgag[count_i-1]["data-src"]
            }
        )
    
    # print("complete request")
    return data_site


def AcDcParser(url):
    # print("request to AcDc")

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")

    imagag = soup.find_all("img",{"class":"card-img-top"})
    
    count_i = 0
    for content_data in soup.find_all("div",{"class":"card-body"}):
        
        title = content_data.find("h3").text
        date = content_data.find("span").text

        title = title.replace("\n","")
        date  = date.replace("\n","")
    
        data_site["AcDc"].append(
            {
                "title":title,
                "date":date,
                "img":imagag[count_i]["src"]
            }
        )
        count_i = count_i + 1


    # print("complete request")
    return data_site

def SaveToJson(data_site):

    json_data = json.dumps(data_site)
    file = open(pwdJson,"w")
    file.write(json_data)




