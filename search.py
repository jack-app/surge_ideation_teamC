from googleapiclient.discovery import build
import requests, json 
import pprint
from dotenv import load_dotenv
import os
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
    return Result
print(songle_search('yoasobi アイドル'))

