from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from iycf_model import IycfModel
from numpy import array
from fastapi.responses import HTMLResponse
import os
import shutil

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

class_predications = array(['123123', '607000', '607001'])

@app.get("/home")
async def home():


    return {"message": "Welcome to IYCF Image Vision API!"}


@app.post("/image/classification/predication")
async def predict_classification(file: UploadFile= File(description="A file read as UploadFile")):
    print("****OK****?")
    if file.filename:
        #fn = os.path.basename(file.filename)
        fn = os.path.join('./files', file.filename)
        with open(fn, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
    return {"filename": file.filename}

@app.get("/")
async def main():
    content = """
<body>
<form action="/image/classification/predication/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(8002), reload=True, workers=2)