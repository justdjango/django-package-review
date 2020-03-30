from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from allauth.account.views import confirm_email
from .views import UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('me/', UserDetailView.as_view())
]
