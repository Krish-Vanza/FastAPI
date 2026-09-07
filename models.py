from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int


    # no need for init method as we are using pydantic BaseModel, it will handle the initialization and validation of the fields automatically.
# """
# def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity = quantity
# """