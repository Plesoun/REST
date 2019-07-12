from src.user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, passsword):
    user = User.find_user_by_name(username)
    if user and safe_str_cmp(user.password, passsword):
        return user
    else:
        return "User not found"


def identity(payload):
    user_id = payload["identity"]
    return User.find_user_by_id(user_id)
