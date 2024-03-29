import sys
sys.path.append('..')
from django.core import management;
import settings;
management.setup_environ(settings)
from socialize.models import Application, ApiUser, ApiUserProfile, Entity, Comment, Consumer

def play_initial_insert():
    print "INITIAL application and user:"
    app = Application(name="Harpie Goes To Sleep.")
    app.consumer = Consumer()
    app.save()
    print "  - App saved: %s" % app
    
    user = ApiUser(first_name="Harp")
    user.profile = ApiUserProfile(device_name='Android')
    user.save()
    print "  - User saved: %s" % user
    print ''
    
def insert_entity():
    print "CREATE entity"
    app = Application.objects.all()[0]
    print app
    print "  - create entity"
    entity = Entity(key="http://harpb.com")
    print "  - set app"
    #entity.application_id = app.id
    entity.application = app
    #entity.application = Application(name='hey')
    print "  - save entity"
    entity.save()
    print entity
    print ''
    
def get_entities():
    entities = Entity.objects.all()
    print "All entities: %s" % entities
    print ''
    
def delete_entities():
    print "DELETE entities"
    entities = Entity.objects.all()
    print "Deleting... %s" % entities
    entities.delete()
    #for entity in entities:
    #    entity.delete()
    
def insert_comment():
    app = Application.objects.all()[0]
    api_user = ApiUser.objects.filter()[0]
    entity = Entity.objects.all()[0]
    comment = Comment(text="Harp's first comment")
    comment.application = app
    comment.user = api_user
    comment.entity = entity
    comment.save()
    print comment

def delete_comments():
    comments = Comment.objects.all()
    print "Deleting... %s" % comments
    comments.delete()

play_initial_insert()   
insert_entity()
get_entities()
insert_comment()
delete_comments()
delete_entities()  

print "\n ALL APPS"
apps = Application.objects.all()
for app in apps:
    app