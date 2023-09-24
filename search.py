from googleapiclient.discovery import build
import requests, json 
import pprint
from dotenv import load_dotenv
import os
from fastapi import FastAPI
import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './account_key.json'

# songleにurlがあるかを判定する。boolを返す
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
    
# ユーチューブAPIから動画のjsonを取得する。
def song_search(retrieval):
    # APIKEYを取得する
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    # video_id_listの初期化
    
    SEARCH_QUELY = retrieval
    
    # リスポンスの取得
    request = youtube.search().list(
    q=SEARCH_QUELY, 
    part='id,snippet',
    maxResults=50,
    type='video',
    videoDuration='medium', 
    order='viewCount',
    videoCategoryId=10,
    regionCode='jp',
    )
    response = request.execute()
    return response

# responseのjsonを渡すとtitleとurlのdictが返る
def video_url(response):
    video_id_list = []
    video_id_title= []
    video_id_list.extend(list(map(lambda v : v['id']['videoId'],response['items'])))
    video_id_title.extend(list(map(lambda v : v['snippet']['title'],response['items'])))
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))
    result = dict(zip(video_id_title,video_id_list))
    return result
# response(json)を渡すとtitileと動画idのdictが返る
def video_id(response):
    video_id_list = []
    video_id_title= []
    video_id_list.extend(list(map(lambda v : v['id']['videoId'],response['items'])))
    video_id_title.extend(list(map(lambda v : v['snippet']['title'],response['items'])))
    result = dict(zip(video_id_title,video_id_list))
    return result
# titleとurlを渡せばsongleにあるsongleあるurlだけ部分のurlを返す。
def songle_check(titileurl):
    
    Result={}
    for title ,url  in titileurl.items():
        if songle_in(url) is True:
            Result.setdefault(title,url)
        else :
            None
    return Result 


def songle_decheck(titileurl):
    
    Result={}
    for title ,url  in titileurl.items():
        if songle_in(url) is True:
            None
        else :
            Result.setdefault(title,None)
    return Result 

# songleからsongのサビurlを取得
def songle_se(Result):
    Result=songle_check(Result)
    surbeurl = {}
    Api_EndPoint = 'https://widget.songle.jp/api/v1/song/chorus.json'
    headers = {"Content-Type": "application/json"}
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
# 検索文字列を打てばタイトルとサビのdictの部分を返す
def songle(query):
     data=video_url(song_search(query))
     response=songle_se(data)
     return response
# 
def songle_in_url(query):
    data = video_url(song_search(query))
    response=songle_check(data)
    return response



# q = input('好きなアーティストを入力してください')
# pprint.pprint(songle(q))



def get_video_id_in_playlist(playlistId):
    # youtubesetup
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
        maxResults=50,
        playlistId=playlistId,
        fields="nextPageToken,items/snippet"
    )
    while request:
        response = request.execute()
        video_id_list.extend(list(map(lambda item: item["snippet"]["resourceId"]["videoId"], response["items"])))
        
        request = youtube.playlistItems().list_next(request, response)
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))
# playlistid でtitleとurlのdictが返る
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
        maxResults=50,
        playlistId=playlistId,
        fields="nextPageToken,items/snippet"
    )
    response=request.execute()
    video_id_list.extend(list(map(lambda v : v['snippet']['resourceId']['videoId'],response['items'])))
    video_id_list=list(map(lambda v: "https://www.youtube.com/watch?v="+v , video_id_list ))
    video_title_list.extend(list(map(lambda v : v['snippet']['title'],response['items'])))
    result = dict(zip(video_title_list,video_id_list))
    return result
# playlistidでサビ部分とurlのdictが返る
def get_video_id_all_playlist_in_songle(playlistId):
    result=get_video_id_all_playlist(playlistId)
    subi=songle_se(result)
    return subi
# channekid　でchannelのsnnipetとcontentDetailsが返る
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
# channelIdでplaylistのtitleとplaylistidのdictが返る
def channel_playlist_ID(channelid):
    API_KEY=os.getenv('API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY)
    request = youtube.playlists().list(
        part="snippet,id",
        channelId=channelid,
    )
    response=request.execute()
    palylist_Id_list = list(map(lambda v : v['id'],response['items'] ))
    playlist_title_list = list(map(lambda v : v['snippet']['title'] , response['items']))
    palylist_dict = dict(zip(playlist_title_list,palylist_Id_list ))
    return palylist_dict



API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube"]
CLIENT_SECRETS_FILE = 'client_secret_44130362195-7j4dnus14loc9s3r30pjhmfjv9fqs19j.apps.googleusercontent.com.json'

PLAYLIST_ID='PLcG4kHrgRmgm5dIUofGqC1hHS8dzx6iF6'

KEYWORD_ARRAY =[]
KEYWORD_ARRAY.append('')
KEYWORD_ARRAY.append('')
KEYWORD_ARRAY.append('')

# https://dev.classmethod.jp/articles/oauth2client-is-deprecated/ より引用
# youtubeをsetup
def youtube_setup():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)


def searchVideosByKeywords(youtube,keywords,strLastWeek):
    videoIdArray = []
    for keyword in keywords:    
        searchResponse = youtube.search().list(
            q=keyword,
            part='snippet',
            type='video',
            regionCode='jp',
            maxResults=1,
            publishedAfter=strLastWeek,
            ).execute()
        sr = searchResponse['items'][0]
        snippetInfo = sr['snippet']
        title = snippetInfo['title']
        channelTitle = snippetInfo['channelTitle']
        videoIdArray.append(sr['id']['videoId'])
    return videoIdArray

# youtubeにvideoIDのリストをpalylistの中に入っているか入っていないかを判定して、動画idを入れることができる。

def insertVideosIntoPlaylist(youtube,playlistItem_list_response,videoIdArray,PLAYLIST_ID):
    videoAlready = []
    for item in playlistItem_list_response["items"]:
        videoAlready.append(item["snippet"]["resourceId"]["videoId"])

    for id in videoIdArray:
        if id not in videoAlready:
            playlistItem_insert_response = youtube.playlistItems().insert(
            part="snippet,status",
            body=dict(
                snippet=dict(
                    playlistId=PLAYLIST_ID,
                    resourceId=dict(
                        videoId=id,
                        kind="youtube#video",
                    )
                )
            )
            ).execute()

def main(PLAYLIST_ID):
    
    youtube = youtube_setup()


    dtNow = datetime.datetime.now()
    dtLastWeek = dtNow - datetime.timedelta(days=7)
    strLastWeek = dtLastWeek.strftime(f'%Y-%m-%dT%H:%M:%SZ')

    videoIdArray = searchVideosByKeywords(youtube,KEYWORD_ARRAY,strLastWeek)

    playlistItem_list_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=PLAYLIST_ID,
        maxResults = 50,
    ).execute()

    insertVideosIntoPlaylist(youtube,playlistItem_list_response,videoIdArray)

    print("done")
# channelに空のplaylist1を作る
def create_newplaylist(titlename):
    youtube=youtube_setup()
    # This code creates a new, private playlist in the authorized user's channel.
    playlists_insert_response = youtube.playlists().insert(
    part="snippet,status",
    body=dict(
        snippet=dict(
        title=titlename,
        description="A private playlist created with the YouTube API v3"
        ),
        status=dict(
        privacyStatus="private"
        )
    )
    ).execute()
    return playlists_insert_response["id"]

def search_by_keywords(keywards,emotion):
    PLAYLIST_ID=create_newplaylist(emotion)
    url=songle_in_url(keywards)
    youtube=youtube_setup()
    playlistItem_list_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=PLAYLIST_ID,
        maxResults = 50,
    ).execute()
    urls = list(url.values())
    urls = map(lambda v : v.replace("https://www.youtube.com/watch?v=",'',1),urls)
    insertVideosIntoPlaylist(youtube,playlistItem_list_response,urls,PLAYLIST_ID)
    return print('done')
# q = input('ここにアーティスト名を検索')
# e = input('ここに感情名を記入')
# search_by_keywords(q,e)


# ここは自分用
# def youtube_search(retrieval):
#     # APIKEYを取得する
#     youtube=youtube_setup()
#     # video_id_listの初期化
    
#     SEARCH_QUELY = retrieval
    
#     # リスポンスの取得
#     request = youtube.search().list(
#     q=SEARCH_QUELY, 
#     part='id,snippet',
#     maxResults=10,
#     type='video',
#     videoDuration='medium', 
#     order='viewCount',
#     regionCode='jp',
#     )
#     response = request.execute()
#     return response

# def youtube_search_url(query):
#     data = video_url(youtube_search(query))
#     return data 

def search_Keyword(keywords):
    PLAYLIST_ID=create_newplaylist(keywords)
    url=youtube_search_url(keywords)
    youtube=youtube_setup()
    playlistItem_list_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=PLAYLIST_ID,
        maxResults = 50,
    ).execute()
    urls = list(url.values())
    urls = map(lambda v : v.replace("https://www.youtube.com/watch?v=",'',1),urls)
    insertVideosIntoPlaylist(youtube,playlistItem_list_response,urls,PLAYLIST_ID)
    return print('done')

def songle_check_in_or_None(titileurl):
    
    Result={}
    for title ,url  in titileurl.items():
        if songle_in(url) is True:
            Result.setdefault(title,url)
        else :
            Result.setdefault(title,None)
    return Result 

def title_songle_depart(playlistId):
    All_playlist_title_url=get_video_id_all_playlist(playlistId)
    All_playlist_songle_url=get_video_id_all_playlist_in_songle(playlistId)
    for title in All_playlist_title_url.keys():
        if title in All_playlist_songle_url:
            All_playlist_title_url[title]=All_playlist_songle_url[title]
        else:
            All_playlist_title_url[title]=None
    return All_playlist_title_url

def emotion_songle_in(PLAYLIST_ID,myplaylistID):
    url = get_video_id_all_playlist(PLAYLIST_ID)
    url=songle_check(url)
    youtube= youtube_setup()
    playlistItem_list_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=myplaylistID,
        maxResults = 50,
    ).execute()
    urls = list(url.values())
    urls = map(lambda v : v.replace("https://www.youtube.com/watch?v=",'',1),urls)
    insertVideosIntoPlaylist(youtube,playlistItem_list_response,urls,myplaylistID)
    return print('done')

# print(create_newplaylist('悲しい'))

emotion_songle_in('PL_yex3sFlQmV1y6VxZ-FN-FRxb_e-tW6f','PLcG4kHrgRmgmwi2nF2Y3MVhORdXqWVlQS')


