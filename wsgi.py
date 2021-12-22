# pylint: disable=missing-docstring

from flask import Flask, jsonify, request
from config import Config

from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

from ext.orm import db, ma
db.init_app(app)
ma.init_app(app)

from models import Product

migrate = Migrate(app, db)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200


from schemas import many_product_schema, one_product_schema

@app.route(f'{Config.BASE_URL}/products', methods=['GET'])
@app.route(f'{Config.BASE_URL}/products/<int:id>', methods=['GET'])
def get_products(id=None):
    if id:
        product = db.session.query(Product).get(id) # SQLAlchemy request => 'SELECT * FROM products WHERE id = {id}'
        if product: 
            return one_product_schema.jsonify(product), 200
        else:
            return jsonify({"message": f"Product {id} not found"}), 404
    else:
        products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
        return many_product_schema.jsonify(products), 200

@app.route(f'{Config.BASE_URL}/products', methods=['POST'])
def create_product():

    data = request.json

    if isinstance(data, dict) and data.get("name"):
        product = Product()
        product.name = data.get("name")
        product.description = data.get("description")

        db.session.add(product)
        db.session.commit()

        return one_product_schema.jsonify(product), 200
    else:
        return jsonify({"message": "Unprocessable Entity" }), 422


@app.route(f'{Config.BASE_URL}/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    if not id is None:
        product = db.session.query(Product).get(id) # SQLAlchemy request => 'SELECT * FROM products WHERE id = {id}'
        if not product is None: 
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": f"Product {id} deleted"}), 200
    return jsonify({"message": f"Product {id} not found"}), 404
