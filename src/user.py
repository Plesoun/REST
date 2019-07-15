import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_user_by_name(cls, username):
        connection = sqlite3.connect(
            "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db"
        )
        querry = f"SELECT * FROM users WHERE username=?"

        cursor = connection.cursor()
        result = cursor.execute(querry, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_user_by_id(cls, _id):
        connection = sqlite3.connect(
            "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db"
        )
        querry = "SELECT * FROM users WHERE id=?"

        cursor = connection.cursor()
        result = cursor.execute(querry, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


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

        if User.find_user_by_name(data["username"]):
            return {"message": "Username already exists"}, 400

        connection = sqlite3.connect(
            "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db"
        )
        cursor = connection.cursor()

        querry = "INSERT INTO users VALUES (NULL, ?, ?)"

        cursor.execute(querry, (data["username"], data["password"]))

        connection.commit()
        connection.close()

        return {"message": "User successfully created"}, 201
