import requests
import json, time

def apiGetJSON(jsonURL):
    jRes = requests.get(jsonURL)
    jRes1 = jRes.text
    return jRes1

def apiGetImage(imageURL, id):
    file_name = "new" + str(id) + "file.png"
    iRes = requests.get(imageURL)
    f = open(file_name, "wb")
    f.write(iRes.content)
    return "OK"
