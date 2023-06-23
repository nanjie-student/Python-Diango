from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    #msg = 'Hello, you are on the projects page'
    #'message' is key, msg is variable name
    #return render(request, 'projects/projects.html',{'message': msg})
    # page = 'projects'
    # number = 10
    projects = Project.objects.all()
    context  = {'projects': projects}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html',{'project': projectObj})

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request,"projects/project_form.html",context);
