from googleapiclient.discovery import build
import requests, json 
import pprint
from dotenv import load_dotenv
import os
# ユーチューブAPIから動画のurlを取得する。

def emotion(retrieval,emotion):
    load_dotenv()
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    # 検索するべき値の代入
    SEARCH_QUELY = retrieval
    
    # リスポンスの取得
    response = youtube.search().list(
    q=SEARCH_QUELY, 
    part='id', 
    maxResults=1,
    type='video',
    videoDuration='medium', 
    order='viewCount'
    ).execute()
    
    # リスポンスから動画idの取得
    response.setdefault('emotion',emotion)
    items = response['items']
    lists_items = items[0]
    id = lists_items['id']  
    videoid=id['videoId']

    return 'https://www.youtube.com/watch?v='+videoid
    # return pprint.pprint(response)

def songle_search(retrival,emotion):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    


def playlist(retrieval):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)

    response = youtube.playlists().list(
        part='id,player,snippet',
        maxResults=1,
        id = retrieval
    ).execute()
    return pprint.pprint(response)

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
        fields="nextPageToken,items/snippet/resourceId/videoId"
    )

    while request:
        response = request.execute()
        video_id_list.extend(list(map(lambda item: item["snippet"]["resourceId"]["videoId"], response["items"])))
        request = youtube.playlistItems().list_next(request, response)
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))

    return video_id_list

# プリント
def songle_se(playlistedId):
    Api_EndPoint = 'https://widget.songle.jp/api/v1/song/chorus.json'
    headers = {"Content-Type": "application/json"}
    
    def songle_in(url):
        url = {'url':url}
        json_url = json.dumps(url)
        #songleからサビのデータを取得⇒データの変換
        sabi = requests.get(Api_EndPoint, headers=headers,data=json_url)
        
        if str(sabi) == '<Response [200]>':
            return True
        else:
            return False
    video_id_list = get_video_id_in_playlist(playlistedId)
    video_id_list = list(filter(lambda v:songle_in(v),video_id_list))
    for url in video_id_list:
        url = {'url':url}
        json_url = json.dumps(url)
        #songleからサビのデータを取得⇒データの変換
        sabi = requests.get(Api_EndPoint, headers=headers,data=json_url)
        json_sabi = json.loads(sabi.text)
        start = json_sabi['chorusSegments'][0]['repeats'][0]['start']
        end = start + json_sabi['chorusSegments'][0]['repeats'][0]['duration']
        print("開始時刻は"+str(start))
        print("終わりの時刻は"+str(end))

playlist=input('playlist>>>>')
songle_se(playlist)
#APIを使う準備










