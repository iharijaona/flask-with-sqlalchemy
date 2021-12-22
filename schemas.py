# pylint: disable=missing-docstring

from ext.orm import ma
from models import Product

class ProductSchema(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description') # Ce sont les champs que nous voulons dans le JSON !

one_product_schema = ProductSchema()
many_product_schema = ProductSchema(many=True)