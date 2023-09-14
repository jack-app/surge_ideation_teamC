from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status, Response
from firebase_admin import auth, credentials

import firebase_admin
import requests

from dotenv import load_dotenv
import os

# 環境変数を構成
load_dotenv()
API_KEY = os.getenv("API_KEY")

# firebaseを構成
cred = credentials.Certificate('./account_key.json')
firebase_admin.initialize_app(cred)

# トークンを取得
def get_user_token(email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=" + API_KEY
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    return requests.post(url=url, json=data).json()

# ユーザー情報を取得
def get_user(res: Response, cred: HTTPAuthorizationCredentials=Depends(HTTPBearer(auto_error=False))):
    print("ready", cred)
    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
        decoded_token = auth.verify_id_token(cred.credentials)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
        )
    res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'
    return decoded_token
