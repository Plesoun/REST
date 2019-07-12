import sqlite3
from flask_restful import Resource


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_user_by_name(cls, username):
        connection = sqlite3.connect("database.db")
        querry = f"SELECT * FROM users WHERE username={(username,)}"

        cursor = connection.cursor()
        result = cursor.execute(querry)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_user_by_id(cls, _id):
        connection = sqlite3.connect("database.db")
        querry = f"SELECT * FROM users WHERE id={(_id,)}"

        cursor = connection.cursor()
        result = cursor.execute(querry)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    pass
