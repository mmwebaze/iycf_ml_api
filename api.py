from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from iycf_model.IycfModel import IycfModel
from fastapi.responses import HTMLResponse
import os
import shutil

API_VERSION = "v1"

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

@app.get("/api/v1/home")
async def home():


    return {"message": "Welcome to IYCF Image Vision API!"}

@app.post("/api/v1/caption")
async def generate_caption():

    return {"caption": "Caption end-point not yet implemented"}

@app.post("/api/v1/prediction")
async def predict_classification(file: UploadFile= File(description="A file read as UploadFile")):
    print("****OK****?")
    if file.filename:
        #fn = os.path.basename(file.filename)
        fn = os.path.join('./files', file.filename)
        with open(fn, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        model = IycfModel('iycf_model_v4.h5')
        return model.predict_class(file.filename)
        #return {"filename": file.filename}
    return {"message": "No image provided!"}

@app.get("/")
async def main():
    result = await home()

    return result

# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/image/classification/predication/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
    #return HTMLResponse(content=content)

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(8002), reload=True, workers=2)