import requests
import os
from dotenv import load_dotenv
import datetime
import base64

# .envファイルのパスを指定して読み込む
load_dotenv('.env')

# 環境変数を利用する
TOKEN = os.getenv('TOKEN')
OWNER = os.getenv('OWNER')
REPO = os.getenv('REPO')
PATH = os.getenv('PATHs')
SHA_MAIN = os.getenv('SHA_MAIN')  # SHAを取得しておく


url = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}'

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f'Bearer {TOKEN}',
    "X-GitHub-Api-Version": "2022-11-28"
}
response = requests.get(url, headers=headers)

# リクエストボディ
content = base64.b64encode(str(datetime.datetime.now()).encode()).decode()  # Base64でエンコードされた内容をデコードして文字列にする

datum = {
    "message": "my commit message",
    "committer": {"name": "yufoxda", "email": "mysubaccoun1@gmail.com"},
    "content": content,  # Base64でエンコードされた内容
    "sha": response.json().get("sha")  # 取得したSHAを使う
}

# PUTリクエストを送信
response = requests.put(url, headers=headers, json=datum)

# ステータスコードを確認
print(response.status_code)  # 200なら成功

# レスポンスの内容（JSON）を表示
print(response.json())
