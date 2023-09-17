from fastapi import FastAPI, Depends
from user import get_user, get_user_token

# FastAPIを構成
app = FastAPI()

@app.post("/get_token")
def hoge():
    return get_user_token("tomoki826.movie@gmail.com", "Ccl914721")

@app.get("/api/")
async def hello():
    return {"msg":"Hello, this is API server"} 

# トークンをチェックする
@app.get("/api/me")
async def hello_user(user = Depends(get_user)):
    return {"msg":"Hello, user","uid":user['uid']} 
