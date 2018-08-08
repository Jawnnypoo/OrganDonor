import requests
import json
import urllib
import argparse
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

    response = requests.request(
        "POST", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    link = data["link"]
    title = data["title"]
    print("Downloading " + link)

    file_name = title + ".mp3"
    urllib.urlretrieve(link, file_name)
    return file_name


parser = argparse.ArgumentParser(
    description='Download YouTube to MP3, upload to GPlay Music')
parser.add_argument('video', metavar='video', type=str,
                    help='the YouTube video url')

parser.add_argument('-d', action='store_true',
                    help='debug mode')

args = parser.parse_args()

video = args.video
debug = args.d

# Download the file
name = download_video(video)

if debug:
    print("Exiting before upload, since debug")
    sys.exit(0)
mm = Musicmanager()
login_result = mm.login()
if login_result is False:
    mm.perform_oauth(open_browser=True)
# now we are ready to upload
print("Uploading " + name)
result = mm.upload(filepaths=name)
# TODO tell if success or not
