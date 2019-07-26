#!/usr/bin/env python3
from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from src.log_in import authenticate, identity
from src.user import UserRegister
from src.items import Item, ItemsAll

app = Flask(__name__)
app.secret_key = "test"
api = Api(app)

# render_template('hello.html')

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, "/item/<string:name>")
api.add_resource(UserRegister, "/register")
api.add_resource(ItemsAll, "/items")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
