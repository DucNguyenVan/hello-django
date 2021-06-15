from django.http.response import HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse


from ..models import Tag
from ..forms import TagForm

def index(request):
    tags = Tag.objects.all()
    
    return render(request, 'tag/index.html', {"tags": tags})

def detail(request, pk):
    tag = Tag.objects.get(pk=pk)

    return render(request, 'tag/detail.html', {"tag": tag})

def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tag_index'))
    else:
        form = TagForm()

    return render(request, 'tag/new.html', {'form': form})