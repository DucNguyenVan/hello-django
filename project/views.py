import project
from django.shortcuts import render

from project.models import Project
# Create your views here.

def index(request):
    project_list = Project.objects.all()

    return render(request, "project/index.html", {"projects": project_list})

def detail(request, pk):
    project = Project.objects.get(pk=pk)

    return render(request, "project/detail.html", {"project": project})