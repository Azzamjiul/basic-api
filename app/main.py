from typing import Optional
from fastapi import FastAPI, Header
from app.settings import settings
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

@app.get("/")
def hello(max_price: Optional[int] = None, x_token: str = Header(None)):
    return {
        "message": "Hello, World!",
        "max_price": max_price,
        "x_token": x_token
    }

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )