import api.service.get_env_var as v
import requests
import base64
def get_file():
    url = f'https://api.github.com/repos/{v.OWNER}/{v.REPO}/contents/{v.PATH}'

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f'Bearer {v.TOKEN}',
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        content = response.json().get("content")
        if content:
            # base64でエンコードされた内容をデコード
            decoded_content = base64.b64decode(content)
            
            # SQLiteファイルとして保存
            with open("ompooscores.db", "wb") as db_file:
                db_file.write(decoded_content)
            
            return 200
        
    return -1
