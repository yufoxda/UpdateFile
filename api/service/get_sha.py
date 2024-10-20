import api.service.get_env_var as v
import requests

def get_sha():
    url = f'https://api.github.com/repos/{v.OWNER}/{v.REPO}/contents/{v.PATH}'

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f'Bearer {v.TOKEN}',
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("sha")
    else:
        print(f"SHA取得エラー: {response.status_code}")
        print(f"レスポンス: {response.json()}")
        return None
