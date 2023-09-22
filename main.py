from fastapi import FastAPI, Request
from pydantic import BaseModel
from oauth2client.client import OAuth2WebServerFlow
from fastapi.responses import RedirectResponse
from googleapiclient.discovery import build

import json
import httplib2

from dotenv import load_dotenv
import os

from search import create_newplaylist, channel_playlist_ID, get_video_id_all_playlist

# 環境変数を構成
load_dotenv()
FIRESTORE_API_KEY = os.getenv("FIRESTORE_API_KEY")

# from search import get_video_id_all_playlist
from starlette.middleware.cors import CORSMiddleware # 追加

app = FastAPI()

# オリジン情報を読み込む
FRONTEND_ORIGIN = "http://localhost:8080"
BACKEND_ORIGIN  = "http://127.0.0.1:8000"

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

#playlistの通信
class PlaylistID(BaseModel):
    playlistID: str

# クライアント情報を読み込む
CLIENT_SECRETS_FILE = "./secret/youtube_secret.json"
with open(CLIENT_SECRETS_FILE, 'r') as json_file:
    SECRETS_DATA = json.load(json_file)

# OAuth2.0情報を読み込む
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
REDIRECT_URI = BACKEND_ORIGIN + "/api/callback"

# flowオブジェクトを記載
flow = OAuth2WebServerFlow(
    client_id=SECRETS_DATA["installed"]["client_id"],
    client_secret=SECRETS_DATA["installed"]["client_secret"],
    scope=YOUTUBE_READ_WRITE_SCOPE,
    redirect_uri=REDIRECT_URI
)

class PlaylistID(BaseModel):
    playlistID: str

# プレイリストIDから曲のリストをゲットする
@app.post("/api/playlistid")
async def get_playlistid(data: PlaylistID):
    return get_video_id_all_playlist(data.playlistID)

# グーグル認証画面を作る
@app.get("/api/googleauth")
async def access_googleauth():
    auth_uri = flow.step1_get_authorize_url()
    return auth_uri

# 認証して、対応するチャンネルIDをデータベースに新規登録する
@app.get("/api/callback")
async def handle_auth_callback(request: Request, code: str, scope: str):

    global youtube

    # 認証コードを取得
    credentials = flow.step2_exchange(code)

    # YouTube Data APIクライアントを作成する
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                  YOUTUBE_API_VERSION,
                  http=credentials.authorize(httplib2.Http())
                 )
    
    # トークンを取得
    access_token = credentials.access_token
    refresh_token = credentials.refresh_token

    # チャンネル情報を取得
    youtube.channels().list(part="snippet", mine=True).execute()
    response = youtube.channels().list(part="snippet", mine=True).execute()

    # YouTubeアカウントが登録されていない
    if response['pageInfo']['totalResults'] < 1:
        return RedirectResponse(url=FRONTEND_ORIGIN + "/login?error=YouTubeチャンネルを作成してません")

    # チャンネルIDとチャンネル名・アイコンURLを取得
    channel_id = response["items"][0]["id"]
    channel_name = response["items"][0]["snippet"]["title"]
    icon_url = response["items"][0]["snippet"]["thumbnails"]["high"]["url"]

    # token.pickleファイルを生成する
    import pickle
    with open('./token.pickle', 'wb') as token_file:
        pickle.dump(credentials, token_file)

    # プレイリストを作成する
    playlistID = {
        'happy': None,
        'sad':   None,
        'chill': None,
        'fight': None,
        'like':  None,
        'etc':   None
    }
    # プレイリストが既に存在するか確認する
    playlist_data = channel_playlist_ID(channel_id)
    print(playlist_data)
    for key in playlistID.keys():
        songle_title = 'Surbe専用 - ' + key
        if songle_title in playlist_data.keys():
            # 既にある時はそれを代入する
            playlistID[key] = playlist_data[songle_title]
        else:
            # プレイリストが存在しない場合は新規作成する
            playlistID[key] = create_newplaylist('Surbe専用 - ' + key)

    # リダイレクト
    query_params = {"id": channel_id, "name": channel_name, "icon": icon_url, "token": access_token}
    query_params.update(playlistID)
    redirect_url = FRONTEND_ORIGIN + "/login?" + "&".join([f"{key}={value}" for key, value in query_params.items()])
    return RedirectResponse(url=redirect_url)

# 動画タイトルを検索する
"""
@app.post("/api/youtube/search")
async def search(data: Search):
    return emotion(search, emotion)
"""
