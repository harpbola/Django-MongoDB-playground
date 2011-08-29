from pymongo import Connection
import datetime
connection = Connection()

db = connection['test']
print db.collection_names()

posts = db.postser
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
print posts.insert(post)
for post in posts.find():
    print post
print db.collection_names()
