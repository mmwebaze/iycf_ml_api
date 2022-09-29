from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from iycf_model import IycfModel

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

@app.get("/")
async def home():


    return {"message": "Welcome to IYCF Image Vision API!"}


@app.post("/image/classification/predication")
async def predict_classification(file: bytes = File()):
    with open('image.jpg','wb') as image:
        image.write(file)
        image.close()

    return {"I can be reached: ": "OK"}


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(8002), reload=True, workers=2)