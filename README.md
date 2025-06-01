FastAPI App Runner サンプル
===========================

このリポジトリは、FastAPI アプリを Docker でコンテナ化し、
AWS App Runner で簡単にデプロイするための構成です。

------------------------------------------------------------
[ディレクトリ構成]

fastapi-apprunner/
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md

------------------------------------------------------------
[ローカル開発手順]

1. 仮想環境を作成（任意）

Windows:
> python -m venv venv
> .\venv\Scripts\Activate

macOS/Linux:
$ python3 -m venv venv
$ source venv/bin/activate

2. パッケージのインストール

> pip install -r requirements.txt

3. アプリを起動

> uvicorn main:app --reload

→ http://localhost:8000 にアクセス

------------------------------------------------------------
[Docker ビルド & 実行]

1. Docker イメージをビルド

> docker build -t fastapi-apprunner .

2. コンテナを起動

> docker run -p 8000:8000 fastapi-apprunner

------------------------------------------------------------
[AWS App Runner デプロイ手順]

1. GitHub に push

> git init  
> git add .  
> git commit -m "first commit"  
> git branch -M main  
> git remote add origin https://github.com/your-name/fastapi-apprunner.git  
> git push -u origin main

2. AWS App Runner で新しいサービスを作成
   - ソース：GitHub
   - ポート：8000
   - スタートコマンド：
     uvicorn main:app --host 0.0.0.0 --port 8000

------------------------------------------------------------
[API 動作確認]

GET /
→ http://localhost:8000/

レスポンス例：
{ "message": "PDF Upload API is running" }

POST /upload
→ curl -X POST http://localhost:8000/upload -F "file=@test.pdf"

レスポンス例：
{
  "message": "ファイルを受信しました",
  "filename": "20250601123400_test.pdf",
  "size": 12345
}

------------------------------------------------------------
[ライセンス]
MIT License
