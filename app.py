from flask import Flask, jsonify, request, render_template

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

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html') 

# POST /stores
@app.route('/stores', methods=['POST'])
def createStore():
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)

# GET /stores/<string:name>
@app.route('/stores/<string:storeName>', methods=['GET']) 
def getStoreByName(storeName):
    foundStores = list(filter( lambda store: store['name'] == storeName, stores ))
    if (len(foundStores) == 0):
        return jsonify({ 'msg': 'Store not Found!' })    
    return jsonify({ 'store': foundStores[0] })


# GET /stores
@app.route('/stores', methods=['GET'])
def getStores():
    return jsonify({ 'stores': stores })

# POST /stores/<string:storeName>/items
@app.route("/stores/<string:storeName>/items", methods=['POST'])
def createItemForStore(storeName):
    for store in stores:
        if store['name'] == storeName:            
            requestData = request.get_json() 
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['items'].append(newItem)
            return jsonify({ 'item': newItem })
    return jsonify({ 'msg': 'Store not found!' })

# GET /store/<string:storeName>/items/<string:itemName>
@app.route('/stores/<string:storeName>/items/<string:itemName>', methods=['GET'])
def getStoreItemByName(storeName, itemName):
    foundStores = list(filter( lambda store: store['name'] == storeName, stores ))
    if (len(foundStores) == 0):
        return jsonify({ 'msg': 'Store not Found!' })
    foundItems = list(filter(lambda item: item['name'] == itemName, foundStores[0]['items']))
    if (len(foundItems) == 0):
        return jsonify({ 'msg': 'Item not Found!' })
    return jsonify({ 'item': foundItems[0] })

app.run(port=5000)