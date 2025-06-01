from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # ← 追加！

import os
import shutil
from datetime import datetime

app = FastAPI()

# 🔐 CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ← 本番では URL を限定してね
    allow_credentials=True,
    allow_methods=["*"],  # ← OPTIONS 含めすべて許可
    allow_headers=["*"],  # ← カスタムヘッダーも通す
)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="PDFファイルのみ対応しています")

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"

    save_dir = "uploads"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse({
        "message": "ファイルを受信しました",
        "filename": filename,
        "size": os.path.getsize(file_path)
    })

@app.get("/")
def root():
    return {"message": "PDF Upload API is running"}
