from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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


@app.get("/")
async def home():


    return {"message": "Welcome to IYCF Image Vision API!"}


@app.get("/classify")
async def classify_image():


    return {"I can be reached: ": "OK"}


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(8002), reload=True, workers=2)