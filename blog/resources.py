from django.contrib.auth import get_user_model
from tastypie import fields
from tastypie.resources import ModelResource
from .models import Post

User = get_user_model()


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']


class PostResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'

user_resource = UserResource()
post_resource = PostResource()