import urllib
import urllib.request, urllib.parse
import json
import datetime
projecturl = "https://scrapbox.io/api/pages/dirty-tester/?limit=1000"

req = urllib.request.Request(projecturl)
res = urllib.request.urlopen(req)
jsonData = json.loads(res.read())

def show_title_list():
    for item in jsonData["pages"]:
        title = item["title"]
        print("[" + title + "]")#コピペでリンクになるようにする。

def load_created_title_list():
    startdate = "2020/07/12"
    enddate = "2020/09/30"
    for item in jsonData["pages"]:
        title = item["title"]
        pagetime = datetime.datetime.fromtimestamp(item["created"])
        created = pagetime.strftime("%Y/%m/%d")
        if enddate > created > startdate:
            print("[" + title + "]")#コピペでリンクになるようにする。

def load_created_title_list_2():
    startdate = "2020/07/12"
    enddate = "2020/09/30"
    for item in jsonData["pages"]:
        title = item["title"]
        pagetime = datetime.datetime.fromtimestamp(item["created"])
        created = pagetime.strftime("%Y/%m/%d")
        name = item["user"]["id"]
        #if name != "5c8d0988d52c3100174cd0d2":
        if enddate > created > startdate:
            print("[" + title + "]" + str(name))#コピペでリンクになるようにする。

def load_updated_title_list():
    startdate = "2020/07/12"
    enddate = "2020/09/30"
    for item in jsonData["pages"]:
        title = item["title"]
        pagetime = datetime.datetime.fromtimestamp(item["updated"])
        created = pagetime.strftime("%Y/%m/%d")
        if enddate > created > startdate:
            print("[" + title + "]")#コピペでリンクになるようにする。

if __name__ == "__main__":
    load_created_title_list()
    #load_updated_title_list()
    #show_title_list