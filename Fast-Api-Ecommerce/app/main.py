from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Welcome to the fastapi"}

@app.get("/products/{id}")
def get_products(id:int):
    products = ["Wireless Bluetooth Headphones","Ergonomic Office Chair","Stainless Steel Water Bottle","Running Shoes","Mechanical Gaming Keyboard"]
    return products[id]