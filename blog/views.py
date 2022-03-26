from calendar import day_abbr
from multiprocessing import context
from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog,Category
from django.http import HttpResponse
# Create your views here.

data={
        "blogs":[
            {
                "id":1,
                "title":"komple web geliştirme",
                "image":"1.jpg",
                "is_active":True,
                "is_home":False,
                "description":"Harika bir kurs"
            },
            {
                "id":2,
                "title":"python",
                "image":"2.jpg",
                "is_active":True,
                "is_home":True,
                "description":"Harika bir kurs"
            },
            {
                "id":3,
                "title":"django",
                "image":"3.jpg",
                "is_active":False,
                "is_home":True,
                "description":" Harika bir kurs"
            }]
}

def index(request):
    context={
        "blogs":Blog.objects.filter(is_home=True,is_active=True),
        "categories":Category.objects.all()
    }
    return render(request,"blog/index.html",context)
def blogs(request):
    context={
        "categories":Category.objects.all(),
        "blogs":Blog.objects.filter(is_active=True)
    }
    return render(request,"blog/blogs.html",context)
def blogs_by_category(request,slug):
    context={
        "blogs":Category.objects.get(slug=slug).blog_set.all(),
        "categories":Category.objects.all(),
        "selected_category":slug
    }
    return render(request,"blog/blogs.html",context)
def blogDetails(request,slug):
    blog=Blog.objects.get(slug=slug)
    return render(request,"blog/blogDetails.html",{"blog":blog})