from apiclient.discovery import build
import requests, json 
import pprint

# ユーチューブAPIから動画のurlを取得する。

def emotion(retrieval,emotion):
    
    API_KEY =  #取得したAPIキー
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
    ).execute()
    
    # リスポンスから動画idの取得
    response.setdefault('emotion',emotion)
    items = response['items']
    lists_items = items[0]
    id = lists_items['id']  
    videoid=id['videoId']

    return print(f'https://www.youtube.com/watch?v='+videoid)
    # return pprint.pprint(response)

#入力してもらう部分
search = input('ここに動画のタイトルを入力してください')
em = input('ここに感情を入力してください')

emotion(search,em)


def playlist(retrieval):
    API_KEY = 'AIzaSyA9a4qFMa354f-nhgyHcJmqjl3-AIMtNa8' #取得したAPIキー
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

# playlist('PLR48NTfP0M0PTAHZKWNN_i7iR4Bxal8Uy')





