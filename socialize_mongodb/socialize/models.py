from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField

"""
class Tag(models.Model):
    title = models.CharField(max_length=300)
    
    class Meta:
        db_table = "blog_posts_tags"
        
    def __str__(self):
        return self.title"""
    
class Posts(models.Model):
    author = models.CharField(max_length=300)
    text = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)
    #tags = models.ManyToManyField(Tag)
    
    class Meta:
        db_table = "blog_posts"
    
    def __str__(self):
        #for tag in self.tags.all():
        #    print tag
        return "%s by %s on %s [TAGS: %s]" % (self.text, self.author, self.date, self.tags)
    
    
#===============================================================================
# The user
#===============================================================================
class ApiUserProfile(models.Model):
    # related fields
    # user = models.ForeignKey(User, related_name='profile', unique=True)
    # user agent fields
    device_name = models.CharField(max_length=64, null=True, blank=True) # iPod touch
    platform = models.CharField(max_length=64, null=True, blank=True) # iPhone OS
    platform_version = models.CharField(max_length=64, null=True, blank=True) # 4.3.3
    
    sdk_version = models.CharField(max_length=64, null=True, blank=True) # 1.0.0
    
    language_code = models.CharField(max_length=48, null=True, blank=True) # en
    country_code = models.CharField(max_length=48, null=True, blank=True)  # US
        
    class Meta:
        db_table = "api_user_profile"

class ApiUser(models.Model):
    device_id = models.CharField(max_length=240)
    first_name = models.CharField(max_length=240, null=True, blank=True)
    last_name = models.CharField(max_length=240, null=True, blank=True)
    description = models.CharField(max_length=4096, null=True, blank=True)
    location = models.CharField(max_length=1024, null=True, blank=True)
    large_image = models.CharField(max_length=240, null=True, blank=True)
    medium_image = models.CharField(max_length=240, null=True, blank=True)
    small_image = models.CharField(max_length=240, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)
    meta = models.CharField(max_length=1024, null=True, blank=True)
    profile = EmbeddedModelField(ApiUserProfile)
    
    class Meta:
        db_table = "api_user"

#===============================================================================
# Application
#===============================================================================
class Consumer(models.Model):
    key = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)
    
class Application(models.Model):
    name = models.CharField(max_length=128)
    consumer = EmbeddedModelField(Consumer)
    class Meta:
        db_table = "socialize_application"
    
#===============================================================================
# Common fields of socialize models.
#===============================================================================
class SocializeModel(models.Model):
    application = models.ForeignKey(Application)
    #application = EmbeddedModelField(Application)
    #application_id = models.CharField(max_length=24)
    created = models.DateTimeField(auto_now_add=True, null=True) 
    
    class Meta:
        abstract = True
    
class Entity(SocializeModel):
    # dates
    updated = models.DateTimeField(auto_now=True)
    # The DATA.
    key = models.CharField(blank=False, 
                           null=False, 
                           help_text="Lowercase version", 
                           max_length=4096)
    name = models.CharField(max_length=512)
    original_key = models.CharField(blank=False, 
                                    null=False, 
                                    help_text="The key is saved as it is sent by the user.", 
                                    max_length=4096)
    # activities
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    total_activity = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
           
    class Meta:
        db_table = "socialize_entity"
         
class Activity(SocializeModel):
    # The entity is a foreign key
    entity = models.ForeignKey('Entity')
    #entity = EmbeddedModelField('Entity')
    #entity_id = models.CharField(max_length=24)
    
    location = ListField(blank=True)
    share_location = models.BooleanField(default=1)
    
    # the user is a foreign key
    user = models.ForeignKey('ApiUser')
    #user = EmbeddedModelField('ApiUser')
    #user_id = models.CharField(max_length=24)
    class Meta:
        abstract = True
        
class Comment(Activity):
    
    text = models.TextField()
    deleted = models.BooleanField(default=0, db_index=True)

    activity_type = 'comment'
    
    #objects = CommentManager()
           
    class Meta:
        db_table = "socialize_comment"
    
class Like(Activity):
    
    deleted = models.BooleanField(default=0, db_index=True)

    activity_type = 'like'
    
    #objects = CommentManeager()
           
    class Meta:
        db_table = "socialize_like"
    

class ShareMedium(models.Model):
    name = models.CharField(max_length=128, unique=True)
            
class Share(Activity):
    
    text = models.TextField()
    deleted = models.BooleanField(default=0, db_index=True)
    medium = EmbeddedModelField(ShareMedium)
    
    activity_type = 'share'
    
    #objects = CommentManager()
           
    class Meta:
        db_table = "socialize_share"
    
        
class View(Activity):
    
    activity_type = 'view'
    
    #objects = CommentManager()
           
    class Meta:
        db_table = "socialize_view"
    