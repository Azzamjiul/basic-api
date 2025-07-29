from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.settings import settings
from app.routes.products import products_router

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

app.include_router(products_router)

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )