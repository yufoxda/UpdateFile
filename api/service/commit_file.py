import api.service.get_env_var as v
import requests
import base64
from api.service.get_sha import get_sha
import os

def commit_file(new_content: str):
    sha = get_sha()

    if sha is None:
        return {"status": "error", "message": "SHAの取得に失敗しました"}

    with open("ompooscores.db", "rb") as binary_file:
        binary_data = binary_file.read()
        encoded_data = base64.b64encode(binary_data).decode('utf-8')

    url = f'https://api.github.com/repos/{v.OWNER}/{v.REPO}/contents/{v.PATH}'
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f'Bearer {v.TOKEN}',
        "X-GitHub-Api-Version": "2022-11-28"
    }

    datum = {
        "message": "API経由でのファイル更新",
        "content": encoded_data,
        "sha": sha
    }

    response = requests.put(url, headers=headers, json=datum)

    if response.status_code == 201:
        return {"status": "success", "message": "ファイルの更新に成功しました"}
    else:
        return {"status": "error", "message": response.json()}
