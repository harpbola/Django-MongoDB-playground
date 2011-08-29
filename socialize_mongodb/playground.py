from socialize.models import Posts
from pymongo import Connection
import datetime

def play_insert_post(posts_collection):
    post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
    print posts_collection.insert(post)
    
def play_mongo():
    connection = Connection()
    db = connection['test']
    posts = db.blog_posts
    #play_insert_post(posts)
    for post in posts.find():
        print "Post: %s" % post
    print "Collections: %s" % db.collection_names()
    
def play_posts_model():
    print "All Posts: %s" % Posts.objects.all()

play_mongo()    
play_posts_model()
