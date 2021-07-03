from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Project,tags


# Create your views here.
def index(request):
    projects = Project.all_projects()
    return render(request,'index.html',{"projects":projects})