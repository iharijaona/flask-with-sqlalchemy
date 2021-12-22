# pylint: disable=missing-docstring

from ext.orm import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text())

    def __repr__(self):
        return '<{} : {}>'.format(self.id, self.name)