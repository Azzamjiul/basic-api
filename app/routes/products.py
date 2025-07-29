from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.schema import Product

products_router = APIRouter(prefix="/products", tags=["Product"])

products = [
  Product(id=1, name="Product 1", description="Description 1", price=10.0, category="Category 1"),
  Product(id=2, name="Product 2", description="Description 2", price=20.0, category="Category 2"),
  Product(id=3, name="Product 3", description="Description 3", price=30.0, category="Category 3"),
]

@products_router.get("/", response_model=list[Product])
def get_products():
  return products

@products_router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
  product = None
  for p in products:
    if p.id == product_id:
      product = p
      break
  if product is None:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Product not found")
  return product