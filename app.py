from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from src.log_in import authenticate, identity

app = Flask(__name__)
app.secret_key = "test"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    @jwt_required()
    def get_item(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return (
                {"message": f"An item with a name {name} already exists."},
                400,
            )
