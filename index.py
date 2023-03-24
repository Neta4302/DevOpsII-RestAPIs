import json
from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Soap", "category": 1, "price": 45, "instock": 9000},
    {"id": 2, "name": "Cookie", "category": 2, "price": 90, "instock": 800},
    {"id": 3, "name": "Pineapple", "category": 2, "price": 39, "instock": 1000},
    {"id": 4, "name": "Milk", "category": 2, "price": 49, "instock": 700},
    {"id": 5, "name": "Cooking Pan", "category": 3, "price": 1290, "instock": 300}
]

nextItemId = 6

@app.route('/item', methods=['GET'])
def get_item():
  return jsonify(items)

@app.route('/item/<int:id>', methods=['GET'])
def get_item_id(id: int):
  item = _find_next_id(id)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  return jsonify(item)

def _find_next_id(id: int):
  return next((x for x in items if x['id'] == id), None)

@app.route('/item', methods=['POST'])
def post_item():
  global nextItemId
  item = json.loads(request.data)

  item['id'] = nextItemId
  nextItemId += 1
  items.append(item)

  return '', 201, { 'location': f'/items/{item["id"]}' }

@app.route('/item/<int:id>', methods=['PUT'])
def put_item(id: int):
  item = _find_next_id(id)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  updated_item = json.loads(request.data)
  item.update(updated_item)
  return jsonify(item)

@app.route('/item/<int:id>', methods=['DELETE'])
def delete_item(id: int):
  global items
  item = _find_next_id(id)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  items = [x for x in items if x['id'] != id]
  return jsonify(item), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
