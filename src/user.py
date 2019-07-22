import sqlite3
from flask_restful import Resource, reqparse
from src.mongo_control import MongoControler


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @staticmethod
    def find_user_by_name(username):
        return MongoControler.get_by_username(username)

    @classmethod
    def find_user_by_id(cls, _id):
        return MongoControler.get_by_id(_id)


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be left blank",
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be left blank",
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if MongoControler.get_by_username(data["username"]):
            return {"message": "Username already exists"}, 400

        MongoControler.post_to_userdb(data)

        return {"message": "User successfully created"}, 201
