from django.shortcuts import render
from krigjo25.models import DatabaseProjects, DiscordBots, PythonProjects

def webIndex(request):

    #   Initializing the database connection
    dBotRepo = DiscordBots.objects.all()
    mdb = DatabaseProjects.objects.all()
    
    context = {
                'databases':mdb,
                'dBots': dBotRepo,
                
}

    return render(request, 'index.html', context)


def ProjectDetail(request, pk):

    project = PythonProjects.objects.get(pk=pk)
    context = {'PythonProjects': project,}

    return render(request, 'projectDetail.html', context)

def TestBackGround(request):
    return render(request, 'backGroundTest.html')
