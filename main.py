from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

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
