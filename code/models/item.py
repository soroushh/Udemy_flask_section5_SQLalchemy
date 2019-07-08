import sqlite3
class ItemModel:
    TABLE_NAME = "items"
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name , "price": self.price}
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(*row)
        # if row:
        #     return {'item': {'name': row[0], 'price': row[1]}}

    # @classmethod
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table="items")
        # cursor.execute(query, (item['name'], item['price']))
        cursor.execute(query,(self.name, self.price))

        connection.commit()
        connection.close()

    # @classmethod
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table="items")
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()
