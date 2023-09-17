from fastapi import FastAPI
from src.api.user import get_user_token, delete_user_token, hooge
from pydantic import BaseModel

# FastAPIを構成
app = FastAPI()

# リクエストデータのモデルを作成
class Login(BaseModel):
    email: str
    password: str

class Logout(BaseModel):
    id_token: str

# ログイン情報からトークンを取得
@app.post("/api/login")
async def login(data: Login):
    return get_user_token(data.email, data.password)

# ログアウトする
@app.post("/api/logout")
async def logout(data: Logout):
    delete_user_token(data.id_token)
    return None
