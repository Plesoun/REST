from pymongo import MongoClient

clinet = MongoClient(
    host="mongodb+srv://ples:test@alb-kalae.mongodb.net/test?retryWrites=true&w=majority"
)

db = clinet["alb_1"]

test_post = db["test_post"]

bills_post = test_post.find_one({"title": "Python and MongoDB"})
print(bills_post)

"""
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
"""
# result = test_post.insert_one(post_data)

# print('One post: {0}'.format(result.inserted_id))
