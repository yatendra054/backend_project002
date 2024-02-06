from fastapi import FastAPI,Form,File,UploadFile
import uvicorn
import uuid
import os
from extractor import extract
app = FastAPI()

@app.post("/extract_doc")
def extract_doc(
    file_format : str = Form(...),
    file : UploadFile = File(...),
):
    content = file.file.read()
    file_path="D:/Project_Medical/upload/" + str(uuid.uuid4()) +".pdf"
    with open(file_path,"wb") as f:
        f.write(content)

    data= extract(file_path,file_format)
    if os.path.exists(file_path):
        os.remove(file_path)
    return data;

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
