from fastapi import FastAPI
from pydantic import BaseModel
# from search import get_video_id_all_playlist
from starlette.middleware.cors import CORSMiddleware # 追加

app = FastAPI()

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class PlaylistID(BaseModel):
    playlistID: str

@app.post("/api/playlistid")
async def get_playlistid(data: PlaylistID):
    print(data)
    return "happy"