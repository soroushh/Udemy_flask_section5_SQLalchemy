import sqlite3
from db import db
class ItemModel(db.Model):
    TABLE_NAME = "items"
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name , price):

        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name , "price": self.price}
    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row)
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name
    def save_to_db(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO {table} VALUES(?, ?)".format(table="items")
        # # cursor.execute(query, (item['name'], item['price']))
        # cursor.execute(query,(self.name, self.price))
        #
        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     query = "UPDATE {table} SET price=? WHERE name=?".format(table="items")
    #     cursor.execute(query, (self.price, self.name))
    #
    #     connection.commit()
    #     connection.close()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
