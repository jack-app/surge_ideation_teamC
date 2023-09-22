from googleapiclient.discovery import build
import requests, json 
import pprint
from dotenv import load_dotenv
import os
# ユーチューブAPIから動画のurlを取得する。
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './account_key.json'
def channel_playlist_json(channelid):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=5,
        id=channelid,
    )
    response=request.execute()
    return pprint.pprint(response)
if __name__=='__main__':
    channel_playlist_json('UCrV2uFXLOq1Nf-iG95EHumw')