from fastapi import FastAPI
from pydantic import BaseModel
from search import get_video_id_all_playlist

app = FastAPI()

class PlaylistID(BaseModel):
    playlistID: str

# プレイリストIDから曲のリストをゲットする
@app.post("/api/playlistid")
async def get_playlistid(data: PlaylistID):
    return get_video_id_all_playlist(data.playlistID)