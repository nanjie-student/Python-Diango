from django.shortcuts import render
from django.http import HttpResponse

projectsLists = [
    {
        'id':'1',
        'title': "Ecommerce Website",
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Protfolio Website',
        'description':'This was a project where I build out my portfolio'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awesome open source project I am still working on'
    },
]
def projects(request):
    #msg = 'Hello, you are on the projects page'
    #'message' is key, msg is variable name
    #return render(request, 'projects/projects.html',{'message': msg})
    page = 'projects'
    number = 10
    context  = {'page': page,'number': number,'projects': projectsLists}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = None
    for i in projectsLists:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html',{'project': projectObj})
