from django.contrib import admin
from django.urls import path, include
from home.scheduler import scheduler


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('home.urls')), 
]


scheduler.start()
