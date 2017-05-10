import requests
import json
import urllib
import sys


video = None
if len(sys.argv) > 1:
    video = sys.argv[1]

if video is None:
    print("You need to provide a video url to download")
    sys.exit(1)

url = "http://www.youtubeinmp3.com/fetch/"

querystring = {
    "format": "JSON",
    "video": video
}

headers = {
    'content-type': "application/x-www-form-urlencoded",
}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)

data = json.loads(response.text)

link = data["link"]
title = data["title"]
print(link)

urllib.urlretrieve(link, title + ".mp3")
