from django.shortcuts import render

from ..models import Post, Category

def index(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {'posts': posts}) 

def detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render (request, 'blog/detail.html', {"post": post})

def category(request, category_name):
    category = Category.objects.get(name=category_name)

    return render(request, 'blog/category.html', {'category': category})