from fastapi import FastAPI
from tomoki.api.user import get_user_token, delete_user_token, add_user_account
from tomoki.api.emotion import emotion, playlist
from pydantic import BaseModel

# FastAPIを構成
app = FastAPI()

# リクエストデータのモデルを作成
class Login(BaseModel):
    email: str
    password: str

class Logout(BaseModel):
    id_token: str

class Signup(BaseModel):
    name: str
    email: str
    password: str

class Search(BaseModel):
    search: str
    emotion: str

# ログイン情報からトークンを取得
@app.post("/api/login")
async def login(data: Login):
    return get_user_token(data.email, data.password)

# ログアウトする
@app.post("/api/logout")
async def logout(data: Logout):
    delete_user_token(data.id_token)
    return None

# アカウントを新規作成する
@app.post("/api/signup")
async def signup(data: Signup):
    return add_user_account(data.name, data.email, data.password)

# 動画タイトルを検索する
@app.post("/api/youtube/search")
async def search(data: Search):
    return emotion(search, emotion)