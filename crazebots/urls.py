from django.contrib import admin
from django.urls import path, include, re_path
from home.scheduler import scheduler



# from django.conf.urls import url
from django.conf import settings
from django.views.static import serve



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('home.urls')), 
]


scheduler.start()
