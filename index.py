import json
from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"category": 1, "name": "Chocolate", "price": 80, "instock": 300},
    {"category": 2, "name": "Gummy Bear", "price": 20, "instock": 250},
    {"category": 3, "name": "Milk", "price": 70, "instock": 200},
    {"category": 4, "name": "Ice Cream", "price": 40, "instock": 150},
    {"category": 5, "name": "Coke", "price": 25, "instock": 100}
]

nextItemCategory = 6

@app.route('/item', methods=['GET'])
def get_item():
  return jsonify(items)

@app.route('/item/<int:category>', methods=['GET'])
def get_item_id(category: int):
  item = _find_next_id(category)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  return jsonify(item)

def _find_next_id(category: int):
  return next((x for x in items if x['category'] == category), None)

@app.route('/item', methods=['POST'])
def post_item():
  global nextItemCategory
  item = json.loads(request.data)

  item['category'] = nextItemCategory
  nextItemCategory += 1
  items.append(item)

  return '', 201, { 'location': f'/items/{item["category"]}' }

@app.route('/item/<int:category>', methods=['PUT'])
def put_item(category: int):
  item = _find_next_id(category)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  updated_item = json.loads(request.data)
  item.update(updated_item)
  return jsonify(item)

@app.route('/item/<int:category>', methods=['DELETE'])
def delete_item(category: int):
  global items
  item = _find_next_id(category)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  items = [x for x in items if x['category'] != category]
  return jsonify(item), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
