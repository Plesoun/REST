from mongoengine import *
import json

connect(
    db="alb_1",
    host="mongodb+srv://ples:test@alb-kalae.mongodb.net/test?retryWrites=true&w=majority",
)


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


class MongoControler:
    def __init__(self):
        self.connection = connect(
            db="alb_1",
            host="mongodb+srv://ples:test@alb-kalae.mongodb.net/test?retryWrites=true&w=majority",
        )

    @staticmethod
    def post_to_itemcity(to_post):
        post = ItemCity(**to_post)
        try:
            post.save()

        except ValidationError:
            return {"message": "Input invalid"}

    @staticmethod
    def get_by_item(item_name):
        return ItemCity.objects(item_id=item_name).to_json()

    @staticmethod
    def get_all_objects():
        result = []
        for object in ItemCity.objects:
            result.append(object.to_json())

        return json.dumps(result)
