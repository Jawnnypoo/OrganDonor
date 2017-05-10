import requests
import json
import urllib
import sys
from gmusicapi import Musicmanager


def download_video(youtube_video_url):
    url = "http://www.youtubeinmp3.com/fetch/"

    querystring = {
        "format": "JSON",
        "video": youtube_video_url
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

    file_name = title + ".mp3"
    urllib.urlretrieve(link, title + ".mp3")
    return file_name


video = None
if len(sys.argv) > 1:
    video = sys.argv[1]

if video is None:
    print("You need to provide a video url to download")
    sys.exit(1)

# Download the file
file_name = download_video(video)

mm = Musicmanager()
login_result = mm.login()
if login_result is False:
    mm.perform_oauth(open_browser=True)
# now we are ready to upload
result = mm.upload(filepaths=file_name)
# TODO tell if success or not
