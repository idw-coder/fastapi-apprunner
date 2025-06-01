from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from datetime import datetime

app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="PDFファイルのみ対応しています")

    # ファイル名をユニークにする
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"

    # 保存先ディレクトリ
    save_dir = "uploads"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, filename)

    # ファイル保存
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
