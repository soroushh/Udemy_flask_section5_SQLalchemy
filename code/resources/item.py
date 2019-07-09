from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    # @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        item = ItemModel(None,name, data["price"])

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}

        return item.json()

    # @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "item deleted."}

    # @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            try:
                item = ItemModel(None,name , data["price"])
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                item.price = data["price"]
            except:
                raise
                return {"message": "An error occurred updating the item."}
        # return updated_item
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    TABLE_NAME = 'items'

    @jwt_required()
    def get(self):
        items = []
        for item in ItemModel.find_all():
            items.append(item.json())
        return {"items":items}
