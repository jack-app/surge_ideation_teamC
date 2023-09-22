import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube"]
CLIENT_SECRETS_FILE = 'client_secret_44130362195-7j4dnus14loc9s3r30pjhmfjv9fqs19j.apps.googleusercontent.com.json'
PLAYLIST_ID = "PLcG4kHrgRmgm5C_i5yjzOcBvuD1mymeyY"

KEYWORD_ARRAY =[]
KEYWORD_ARRAY.append('')
KEYWORD_ARRAY.append('')
KEYWORD_ARRAY.append('')

# https://dev.classmethod.jp/articles/oauth2client-is-deprecated/ より引用
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

def insertVideosIntoPlaylist(youtube,playlistItem_list_response,videoIdArray):
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

def main():
    
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

def create_newplaylist():
    youtube=youtube_setup()
    # This code creates a new, private playlist in the authorized user's channel.
    playlists_insert_response = youtube.playlists().insert(
    part="snippet,status",
    body=dict(
        snippet=dict(
        title="Test Playlist",
        description="A private playlist created with the YouTube API v3"
        ),
        status=dict(
        privacyStatus="private"
        )
    )
    ).execute()
    return playlists_insert_response["id"]

if __name__ == "__main__":
    create_newplaylist()
