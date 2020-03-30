from django.contrib import admin
from django.urls import path, include
from tastypie.api import Api
from blog import resources

v1_api = Api(api_name='v1')
v1_api.register(resources.user_resource)
v1_api.register(resources.post_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls))
]
