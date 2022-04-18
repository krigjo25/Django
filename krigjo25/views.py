from django.shortcuts import render
from krigjo25.models import MyProjects

def webIndex(request):

    #   Initializing the database connection
    project = MyProjects.objects.all()
    context = {
                'MyProjects': project,
}

    return render(request, 'index.html', context)

def ProjectDetail(request, pk):

    project = MyProjects.objects.get(pk=pk)
    context = {'MyProjects': project,}

    return render(request, 'projectDetail.html', context)