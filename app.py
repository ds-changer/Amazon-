from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy product data (INR)
products = [
    {"id": 1, "name": "Men's Black T-Shirt", "price": 499, "category": "clothing"},
    {"id": 2, "name": "Women's Red Dress", "price": 999, "category": "clothing"},
    {"id": 3, "name": "Running Shoes", "price": 1999, "category": "shoes"}
]

@app.route("/recommend")
def recommend():
    query = request.args.get("query", "").lower()
    filtered = [p for p in products if query in p["name"].lower()]
    return jsonify(filtered or products)

if __name__ == "__main__":
    app.run(debug=True)
