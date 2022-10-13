from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    stores.append({"name": request_data.get("name"), "items": []})
    return {"message": request_data}, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data.get("name"),
                "price": request_data.get("price"),
            }
            store["items"].append(new_item)
            return {"message": "Item Created successfully", "data": new_item}, 201
    return {"message": "Store Not Found"}, 404


@app.get("/store/<string:name>/item")
def get_store_items(name):
    items = [store for store in stores if store["name"] == name]
    return {"items": items}, 200
