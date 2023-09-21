from googleapiclient.discovery import build
import requests, json 
import pprint
from dotenv import load_dotenv
import os
from fastapi import FastAPI
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './account_key.json'
# ユーチューブAPIから動画のurlを取得する。
def songle_search(retrieval):
    # APIKEYを取得する
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    # video_id_listの初期化
    video_id_list = []
    video_id_title= []
    SEARCH_QUELY = retrieval
    
    # リスポンスの取得
    request = youtube.search().list(
    q=SEARCH_QUELY, 
    part='id,snippet',
    maxResults=5,
    type='video',
    videoDuration='medium', 
    order='viewCount'
    )
    response = request.execute()

    video_id_list.extend(list(map(lambda v : v['id']['videoId'],response['items'])))
    video_id_title.extend(list(map(lambda v : v['snippet']['title'],response['items'])))
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))
    result = dict(zip(video_id_title,video_id_list))
    def songle_in(url):
        Api_EndPoint = 'https://widget.songle.jp/api/v1/song/chorus.json'
        headers = {"Content-Type": "application/json"}
        url = {'url':url}
        json_url = json.dumps(url)
        #songleからサビのデータを取得⇒データの変換
        sabi = requests.get(Api_EndPoint, headers=headers,data=json_url)
        if str(sabi) == '<Response [200]>':
            return True
        else:
            return False
    Result={}
    for title ,url  in result.items():
        if songle_in(url) is True:
            Result.setdefault(title,url)
        else :
            None
    Api_EndPoint = 'https://widget.songle.jp/api/v1/song/chorus.json'
    headers = {"Content-Type": "application/json"}
    surbeurl = {}
    for key , url in Result.items():
        # songle側に渡すurlのjson
        songle_url = {'url':url}
        json_url = json.dumps(songle_url)
        #songleからサビのデータを取得⇒データの変換
        sabi = requests.get(Api_EndPoint, headers=headers,data=json_url)
        json_sabi = json.loads(sabi.text)
        start = int(int(json_sabi['chorusSegments'][0]['repeats'][0]['start'])*(10**-3))
        end = int(int(json_sabi['chorusSegments'][0]['repeats'][0]['start'])*(10**-3)+int(start + json_sabi['chorusSegments'][0]['repeats'][0]['duration'])*(10**-3)+1)

        url=url.replace('watch?v=','embed/',1)
        url = url + '?' + 'start=' + str(start) + '&end=' + str(end)
        surbeurl.setdefault(key,url)
    return surbeurl
def get_video_id_in_playlist(playlistId):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    video_id_list = []
    
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=5,
        playlistId=playlistId,
        fields="nextPageToken,items/snippet"
    )
    while request:
        response = request.execute()
        video_id_list.extend(list(map(lambda item: item["snippet"]["resourceId"]["videoId"], response["items"])))
        
        request = youtube.playlistItems().list_next(request, response)
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))

def get_video_id_all_playlist(playlistId):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    video_id_list = []
    video_title_list = []
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=5,
        playlistId=playlistId,
        fields="nextPageToken,items/snippet"
    )
    response=request.execute()
    # while request:
    #     response = request.execute()
    #     video_id_list.extend(list(map(lambda item: item["snippet"]["resourceId"]["videoId"], response["items"])))
    #     video_title_list.extend(list(map(lambda item : item['snippet']['title'],response["items"])))
    #     request = youtube.playlistItems().list_next(request, response)
    video_id_list.extend(list(map(lambda v : v['snippet']['resourceId']['videoId'],response['items'])))
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))
    video_title_list.extend(list(map(lambda v : v['snippet']['title'],response['items'])))
    result = dict(zip(video_title_list,video_id_list))
    return result
# pprint.pprint(get_video_id_all_playlist('PLNG3n51ur1CeF29__IjcUS09_ME66_pVQ'))
    # return video_id_list
# retrieval = input('Query>>>')
# urls = songle_search(retrieval)
# app = FastAPI()
# @app.get("/")
# async def root():
#     return urls

# https://www.youtube.com/embed/ZRtdQ81jPUQ?start=30&end=40
# https://www.youtube.com/watch?v=
def get_video_id_all_playlist(playlistId):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    video_id_list = []
    video_title_list = []
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=5,
        playlistId=playlistId,
        fields="nextPageToken,items/snippet"
    )
    response=request.execute()
    # while request:
    #     response = request.execute()
    #     video_id_list.extend(list(map(lambda item: item["snippet"]["resourceId"]["videoId"], response["items"])))
    #     video_title_list.extend(list(map(lambda item : item['snippet']['title'],response["items"])))
    #     request = youtube.playlistItems().list_next(request, response)
    video_id_list.extend(list(map(lambda v : v['snippet']['resourceId']['videoId'],response['items'])))
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))
    video_title_list.extend(list(map(lambda v : v['snippet']['title'],response['items'])))
    result = dict(zip(video_title_list,video_id_list))
    def songle_in(url):
        Api_EndPoint = 'https://widget.songle.jp/api/v1/song/chorus.json'
        headers = {"Content-Type": "application/json"}
        url = {'url':url}
        json_url = json.dumps(url)
        #songleからサビのデータを取得⇒データの変換
        sabi = requests.get(Api_EndPoint, headers=headers,data=json_url)
        if str(sabi) == '<Response [200]>':
            return True
        else:
            return False
    Result={}
    for title ,url  in result.items():
        if songle_in(url) is True:
            Result.setdefault(title,url)
        else :
            None
    Api_EndPoint = 'https://widget.songle.jp/api/v1/song/chorus.json'
    headers = {"Content-Type": "application/json"}
    surbeurl = {}
    for key , url in Result.items():
        # songle側に渡すurlのjson
        songle_url = {'url':url}
        json_url = json.dumps(songle_url)
        #songleからサビのデータを取得⇒データの変換
        sabi = requests.get(Api_EndPoint, headers=headers,data=json_url)
        json_sabi = json.loads(sabi.text)
        start = int(int(json_sabi['chorusSegments'][0]['repeats'][0]['start'])*(10**-3))
        end = int(int(json_sabi['chorusSegments'][0]['repeats'][0]['start'])*(10**-3)+int(start + json_sabi['chorusSegments'][0]['repeats'][0]['duration'])*(10**-3)+1)

        url=url.replace('watch?v=','embed/',1)
        url = url + '?' + 'start=' + str(start) + '&end=' + str(end)
        surbeurl.setdefault(key,url)
    return surbeurl

pprint.pprint(get_video_id_all_playlist('PLNG3n51ur1CeF29__IjcUS09_ME66_pVQ'))

