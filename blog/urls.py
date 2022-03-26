from unicodedata import name
from django.urls import URLPattern
from django.urls.conf import path
from . import views
#http://127.0.0.1:8000/ 

urlpatterns=[
path("",views.index,name="home"),
path("index",views.index),
path("blogs",views.blogs,name="blogs"),
path("category/<slug:slug>",views.blogs_by_category,name="blogs_by_category"),
path("blogdetails/<slug:slug>",views.blogDetails,name="blogDetails")
]