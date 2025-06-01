# ベースイメージ（軽量なPython）
FROM python:3.10-slim

# 作業ディレクトリ作成
WORKDIR /app

# 依存ファイルをコピー
COPY requirements.txt .

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY . .

# 起動コマンド（App Runnerはポート8000前提）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
