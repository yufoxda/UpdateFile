import os
from dotenv import load_dotenv

# .envファイルのパスを指定して読み込む
load_dotenv('.env')

# 環境変数を利用する
TOKEN = os.environ['TOKEN']
OWNER = os.environ['OWNER']
REPO = os.environ['REPO']
PATH = os.environ['filePATH']
COMMITER = os.environ['COMMITER']
COMMITER_EMAIL = os.environ['COMMITER_EMAIL']