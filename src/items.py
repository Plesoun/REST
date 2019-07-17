from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
import pandas as pd
from src.mongo_control import MongoControler


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("buy_price_max")
    parser.add_argument("buy_price_min")
    parser.add_argument("city")
    parser.add_argument("item_id")
    parser.add_argument("quality")
    parser.add_argument("sell_price_max")
    parser.add_argument("sell_price_max_date")
    parser.add_argument("sell_price_min")
    parser.add_argument("sell_price_min_date")

    #    @jwt_required()
    def post(self, name):
        data = Item.parser.parse_args()
        MongoControler.post_to_itemcity(data)

    @jwt_required()
    def get(self, name):
        result = self.get_by_name(name)
        if len(result) > 0:
            return result.to_dict(orient="records"), 200

        return {"message": "Item not found"}, 404

    @classmethod
    def get_by_name(cls, name):
        connection = sqlite3.connect(
            "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db"
        )
        query = f"SELECT * FROM items_of_interest WHERE item_id='{name}'"
        result = pd.read_sql(query, connection)
        connection.close()

        return result


class ItemsAll(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect(
            "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db"
        )
        query = f"SELECT * FROM items_of_interest"
        result = pd.read_sql(query, connection)
        connection.close()

        if len(result) > 0:
            return result.to_dict(orient="records"), 200

        return {"message": "Item not found"}, 404
