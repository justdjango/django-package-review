from django.contrib import admin
from django.urls import path, include

from .views import contact

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('contact/', contact)
]
