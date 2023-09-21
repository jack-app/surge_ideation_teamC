from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status, Response
from firebase_admin import auth, credentials, firestore

import firebase_admin
import requests

from dotenv import load_dotenv
import os

# 環境変数を構成
load_dotenv()
FIRESTORE_API_KEY = os.getenv("FIRESTORE_API_KEY")

# firebaseを構成
cred = credentials.Certificate('./account_key.json')
firebase_admin.initialize_app(cred)

# firestoreデータベースを取得
db = firestore.client()

#security = HTTPBearer()

# トークンを取得
def get_user_token(email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=" + FIRESTORE_API_KEY
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    res = requests.post(url=url, json=data).json()
    if 'error' in res:
        return res
        raise HTTPException(status_code=int(res['error']['code']), detail=res['error']['message'])
    doc_ref = db.collection("user").document(res['localId'])
    doc = doc_ref.get()
    res.update(doc.to_dict())
    return res

# トークンを削除
def delete_user_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
        auth.revoke_refresh_tokens(uid)
        print('ユーザーのUID', uid)
    except Exception as e:
        raise HTTPException(status_code=500, detail="ログアウトエラー")

# ユーザーを新規作成
def add_user_account(user_name, email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=" + FIRESTORE_API_KEY
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    res = requests.post(url=url, json=data).json()
    if 'error' in res:
        raise HTTPException(status_code=int(res['error']['code']), detail=res['error']['message'])
    doc_ref = db.collection("user").document(res['localId'])
    doc_ref.set({"name": user_name})
    return res

"""
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
"""