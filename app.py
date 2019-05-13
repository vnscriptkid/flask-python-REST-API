from flask import Flask, jsonify

stores = [
    {
        "name": "pet shop",
         "items": [
             {
                 "name": "dog",
                "price": 100
            },
            {
                "name": "cat",
                "price": 50
            }
         ]
    },
    {
        "name": "tea shop",
        "items": [
            {
                "name": "green tea",
                "price": 150
            },
            {
                "name": "black tea",
                "price": 300
            }
        ]
    }
]

app = Flask(__name__)

# POST /stores
# GET /stores/<string:name>

# GET /stores
@app.route('/stores', methods=['GET'])
def getStores():
    return jsonify({ 'stores': stores })

# POST /stores/<string:storeName>/items
# GET /store/<string:storeName>/items/<string:itemName>


app.run(port=5000)