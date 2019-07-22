from mongoengine import *
import json
import os
import pandas as pd

connect(
    db="test",
    host="mongodb+srv://ples:test@alb-kalae.mongodb.net/test?retryWrites=true&w=majority",
)


class UserDB(Document):
    username = StringField(required=True)
    password = StringField(required=True)


class ItemCity(Document):
    buy_price_max = IntField(min_value=0, required=True)
    buy_price_min = IntField(min_value=0, required=True)
    city = StringField(max_length=30, required=True)
    item_id = StringField(max_length=30, required=True)
    quality = IntField(min_value=0, required=True)
    sell_price_max = IntField(min_value=0, required=True)
    sell_price_max_date = DateTimeField(required=True)
    sell_price_min = IntField(min_value=0, required=True)
    sell_price_min_date = DateTimeField(required=True)


class UserData:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class MongoControler:
    def __init__(self):
        self.item_connection = connect(
            db="test",
            host="mongodb+srv://ples:test@alb-kalae.mongodb.net/test?retryWrites=true&w=majority",
        )

    @staticmethod
    def post_to_userdb(to_post):
        post = UserDB(**to_post)
        try:
            post.save()

        except ValidationError:
            return {"message": "Input invalid"}

    @staticmethod
    def post_to_itemcity(to_post):
        post = ItemCity(**to_post)
        try:
            post.save()

        except ValidationError:
            return {"message": "Input invalid"}

    @staticmethod
    def get_by_username(username):
        result = pd.read_json(UserDB.objects(username=username).to_json())
        result["id"] = result["_id"][0]["$oid"]
        result.drop(["_id"], axis=1, inplace=True)
        result = result.to_dict(orient="records")
        return UserData(
            result[0]["id"], result[0]["username"], result[0]["password"]
        )

    @staticmethod
    def get_by_id(identification):
        result = pd.read_json(UserDB.objects(id=identification).to_json())
        result["id"] = result["_id"][0]["$oid"]
        result.drop(["_id"], axis=1, inplace=True)
        result = result.to_dict(orient="records")
        return UserData(
            result[0]["id"], result[0]["username"], result[0]["password"]
        )

    @staticmethod
    def get_by_item(item_name):
        return ItemCity.objects(item_id=item_name).to_json()

    @staticmethod
    def get_all_objects():
        result = []
        for object in ItemCity.objects:
            result.append(object.to_json())

        return json.dumps(result)
