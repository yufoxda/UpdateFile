import getEnver as v
import requests
import base64

url = f'https://api.github.com/repos/{v.OWNER}/scoremanager5/contents/Database/ompooscores.db'

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
        
        print("SQLiteファイルをダウンロードして保存しました。")
    else:
        print("ファイルのコンテンツが見つかりませんでした。")
else:
    print(f"エラーが発生しました: {response.status_code} - {response.text}")
