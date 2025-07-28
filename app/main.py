from fastapi import FastAPI
from app.settings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

@app.get("/")
def hello():
    return {
        "message": "Hello, World!"
    }
