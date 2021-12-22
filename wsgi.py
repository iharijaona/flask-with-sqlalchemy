# pylint: disable=missing-docstring

from flask import Flask
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


from schemas import many_product_schema

@app.route(f'{Config.BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200