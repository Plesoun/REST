from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
import pandas as pd


class Item(Resource):
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
