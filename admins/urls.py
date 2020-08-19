from django.urls import path
from .import views


urlpatterns = [
    path('', views.admins, name='admins-site2'),#home page url
    
]
