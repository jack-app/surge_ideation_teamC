from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from authlib.integrations.starlette_client import OAuth
import json

app = FastAPI()

# CORS設定
# 異なるオリジン(ドメイン、ポート、プロトコルなど)のHTTPリクエストのブロックを回避
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # フロントエンドのオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuthクライアントの設定
# git ignoreされた機密情報を読み込み
with open('client_secrets.json', 'r') as json_file:
    client_secrets = json.load(json_file)

# OAuthのパラメータを設定
oauth = OAuth()
oauth.register(
    name='google',
    client_id=client_secrets.get('client_id'),
    client_secret=client_secrets.get('client_secret'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    authorize_kwargs=None,
    authorize_extra_params=None,
    token_url='https://accounts.google.com/o/oauth2/token',
    token_params=None,
    token_kwargs=None,
    client_kwargs={'scope': 'openid profile email'},
)

# Google認証を開始するエンドポイント
@app.post("/login")
async def login():
    redirect_uri = '/auth'  # リダイレクトURLをフロントエンドアプリのURLに設定
    return {"auth_url": oauth.google.authorize_redirect_url(redirect_uri)}

# 認証用のエンドポイント
@app.route("/auth")
async def auth(request=Depends(oauth.google)):
    user = await oauth.google.parse_id_token(request)
    # ユーザー情報を取得
    return {"user": user}

# Todoリストの非同期処理
class TodoItem(BaseModel):
    text: str

todos = []

@app.post("/", response_model=TodoItem)
def add_todo(item: TodoItem):
    todos.append(item)
    print("OK")
    return item

@app.get("/", response_model=List[TodoItem])
def get_todos():
    return todos
