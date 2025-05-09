from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()

@app.post("/upload-file")
def uploadFile(file:UploadFile):
    return {"Filename":file.filename}

@app.post("/files")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": file}