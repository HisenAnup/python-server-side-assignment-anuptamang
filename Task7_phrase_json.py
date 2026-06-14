#Parse a JSON file representing product details (name, price, quantity) and display the
#details in tabular format

import json

products = {
    "name": "mouse",
    "price": 1000,
    "quantity": 1
}

# opening json file
with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

lists = []
with open("products.json","r") as files:
    data = json.load(files)
    lists.append(data)

print("name|price|quantity|")    
for each in lists:
    print(f"{each['name']}|{each['price']}|{each['quantity']}|")