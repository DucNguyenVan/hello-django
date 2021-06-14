from django.shortcuts import render 

from ..models import Tag

def index(request):
    tags = Tag.objects.all()
    
    return render(request, 'tag/index.html', {"tags": tags})

def detail(request, pk):
    tag = Tag.objects.get(pk=pk)

    return render(request, 'tag/detail.html', {"tag": tag})