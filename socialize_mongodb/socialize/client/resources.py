from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, Resource
from tastypie.constants import ALL
from tastypie import fields
from socialize.models import Application, ApiUser, Entity, Comment, View, Share,\
    Like, ApiUserProfile

class ClientResource(ModelResource):
    class Meta:
        # auth
        #authentication = PartnerAuthentication()
        #authorization = PartnerAuthorization()
        include_resource_uri = True

class ApiUserProfileResource(ClientResource):
    class Meta(ClientResource.Meta):
        queryset = ApiUserProfile.objects.all()
        
class ApiUserResource(ClientResource):
    #profile = fields.ForeignKey(ApiUserProfileResource, 'profile', full=True)
    class Meta(ClientResource.Meta):
        queryset = ApiUser.objects.all()
        excludes = ['profile']


class ApplicationResource(ClientResource):
    
    class Meta(ClientResource.Meta):
        queryset = Application.objects.all()
        excludes = ['consumer']
        
    def dehydrate_consumer(self, bundle, *args, **kwargs):
        return bundle
    
class EntityResource(ClientResource):
    #application = fields.ForeignKey(ApplicationResource, 'application', full=True)
    
    class Meta(ClientResource.Meta):
        queryset = Entity.objects.all()
        
#===============================================================================
# Activities
#===============================================================================
class ActivityResource(ClientResource):
    #application = fields.ForeignKey(ApplicationResource, 'application', full=True)
    entity = fields.ForeignKey(EntityResource, 'entity', full=True)
    user = fields.ForeignKey(ApiUserResource, 'user', full=True)
    
    class Meta(ClientResource.Meta):
        ordering = ['id']
        filtering = {
                     "id": ALL,
                     "entity": ALL,
                     "user": ALL,
                     "created": ALL,
                     "application": ALL,
                     "lat": ALL,
                     "lng": ALL,
                    }
        
class CommentResource(ActivityResource):
    
    class Meta(ClientResource.Meta):
        queryset = Comment.objects.all()


class LikeResource(ActivityResource):
    
    class Meta(ClientResource.Meta):
        queryset = Like.objects.all()


class ShareResource(ActivityResource):
    
    class Meta(ClientResource.Meta):
        queryset = Share.objects.all()


class ViewResource(ActivityResource):
    
    class Meta(ClientResource.Meta):
        queryset = View.objects.all()


