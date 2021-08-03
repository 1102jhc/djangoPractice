from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('elections.urls')),
    url('admin/', admin.site.urls),
    
]
