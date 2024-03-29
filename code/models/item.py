import sqlite3
from db import db
class ItemModel(db.Model):
    TABLE_NAME = "items"
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, _id, name , price):
        self.id = _id
        self.name = name
        self.price = price

    def json(self):
        return {"id":self.id, "name":self.name , "price": self.price}
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def find_all(cls):
        return cls.query.all()
