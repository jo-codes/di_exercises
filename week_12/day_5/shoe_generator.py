# this file and concept needs to be worked on. I will use JSON as a database for my shopping project, and eventually replace with a DB when we learn it. Now, seeing as it's a small amount of data, I'm going to edit by hand

import json

with open('products.json', 'r+') as f:
    data = json.load(f)

    new_shoe = data['products']

    yeezy = {"id": 5,
             "brand": "yeezy",
             "name": "rock stars",
             "price": 1000
             }

    new_shoe.append(yeezy)

    json.dump(data, f, indent=4)

    print(data["products"])
