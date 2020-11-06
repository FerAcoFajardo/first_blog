from django.urls import path
from .views import *
urlpatterns = [
path('',home,name = 'index'),
path('about-me/',about_me,name ='about_me'),
path('contact/',contact,name ='contact'),
path('posts/',posts,name ='posts'),
path('evidences/',evidences,name='evidences'),
path('<slug:slug>/',detail_post,name ='detail_post'),
]