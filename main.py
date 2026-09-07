from fastapi import FastAPI
from models import Product
from database import session , engine
import database_models

app = FastAPI()

database_models.base.metadata.create_all(bind=engine) # create tables in the database

@app.get("/")
def greet():
    return "Hello, World!" # to web page , we are not printing

products=[
    Product(id=1, name="phone", description="budget phone", price=19.99, quantity=10),
    Product(id=2, name="Laptop", description="Description 2", price=29.99, quantity=5)
]

def init_db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))  # Convert Pydantic model to SQLAlchemy model, model_dump will give you dictionary and need to unpack it to give key value pair
        db.commit()

    
# can make a procucts as a dictionary but we will use models, proper stuff
init_db()

@app.get("/products")
def get_products():
    # db connection with sessionlocal
    db=session();
    # query
    db.query(database_models.Product).all()
    return products

@app.get("/product/{idk}")
def get_product(idk: int):
    for product in products:
        if product.id == idk:
            return product
    return {"error": "Product not found"}

@app.post("/product")
def create_product(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(idk: int, updated_product: Product):
    for i in range(len(products)):
        if products[i].id == idk:
            products[i] = updated_product
            return updated_product
    return {"error": "Product not found"}

@app.delete("/product")
def delete_product(idk: int):
    for i in range(len(products)):
        if products[i].id == idk:
            del products[i]
            return {"message": "Product deleted"}
    return {"error": "Product not found"}