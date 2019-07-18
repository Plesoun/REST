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

    @jwt_required()
    def get(self, name):
        result = MongoControler.get_by_item(name)
        if len(result) > 0:
            return result, 200

        return {"message": "Item not found"}, 404


class ItemsAll(Resource):
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

    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        MongoControler.post_to_itemcity(data)

    @jwt_required()
    def get(self):
        result = MongoControler.get_all_objects()

        if len(result) > 0:
            return result, 200

        return {"message": "Item not found"}, 404
