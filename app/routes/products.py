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

# Create a new product
@products_router.post("/", response_model=Product)
def create_product(new_product: Product):
    # Ensure unique ID
    if any(p.id == new_product.id for p in products):
        raise HTTPException(status_code=400, detail="Product with this ID already exists")
    products.append(new_product)
    return new_product

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


# Update a product completely (PUT)
@products_router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for idx, p in enumerate(products):
        if p.id == product_id:
            products[idx] = updated_product
            return updated_product
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Product not found")

# Update a product partially (PATCH)
@products_router.patch("/{product_id}", response_model=Product)
def patch_product(product_id: int, product_update: dict):
    for idx, p in enumerate(products):
        if p.id == product_id:
            updated = p.model_copy(update=product_update)
            products[idx] = updated
            return updated
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Product not found")

# Delete a product
@products_router.delete("/{product_id}", response_model=dict)
def delete_product(product_id: int):
    for idx, p in enumerate(products):
        if p.id == product_id:
            products.pop(idx)
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Product not found")