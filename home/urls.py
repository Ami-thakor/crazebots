# home/urls.py

from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('pricing', views.pricing_view, name='pricing'),
    path('payment', views.payment_view, name='payment'),
   
    path('success/<data>/', views.success, name='success'),
    path('blog/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
]
