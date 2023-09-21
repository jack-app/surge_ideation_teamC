from fastapi import FastAPI, Request
from pydantic import BaseModel
from backend.search import get_video_id_all_playlist
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from fastapi.responses import RedirectResponse

from googleapiclient.discovery import build

import json
import httplib2

from firebase_admin import auth, credentials, firestore
import firebase_admin

from dotenv import load_dotenv
import os

# 環境変数を構成
load_dotenv()
FIRESTORE_API_KEY = os.getenv("FIRESTORE_API_KEY")

# firebaseを構成
cred = credentials.Certificate('./secret/firebase_secret.json')
firebase_admin.initialize_app(cred)

# firestoreデータベースを取得
db = firestore.client()

# FastAPIを構成
app = FastAPI()

# オリジン情報を読み込む
FRONTEND_ORIGIN = "http://localhost:8080"
BACKEND_ORIGIN  = "http://127.0.0.1:8000"

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
    print(response)

    # YouTubeアカウントが登録されていない
    if response['pageInfo']['totalResults'] < 1:
        return RedirectResponse(url=FRONTEND_ORIGIN + "/login?error=YouTubeアカウントが存在しません")

    # チャンネルIDとチャンネル名・アイコンURLを取得
    channel_id = response["items"][0]["id"]
    channel_name = response["items"][0]["snippet"]["title"]
    print(channel_id)
    print(channel_name)
    icon_url = response["items"][0]["snippet"]["thumbnails"]["high"]["url"]

    # チャンネルIDとチャンネル名・アイコンURLをデータベースに保存
    doc_ref = db.collection("youtube").document(channel_id)
    doc_ref.set({
        "name": channel_name,
        "icon": icon_url
        })

    # プレイリストIDを自動生成・データベースに保存
    
    # (未実装)

    # 生成した各プレイリストIDをデータベースに登録する
    doc_ref.update({
        "happy":    "test",
        "sad":      "test",
        "chill":    "test",
        "fight":    "test",
        "like":     "test",
        "etc":      "test"
    })

    # リダイレクト
    query_params = {"id": channel_id, "name": channel_name, "icon": icon_url, "token": access_token}
    redirect_url = FRONTEND_ORIGIN + "/login?" + "&".join([f"{key}={value}" for key, value in query_params.items()])
    return RedirectResponse(url=redirect_url)