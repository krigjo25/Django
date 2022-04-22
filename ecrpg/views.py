
from django.shortcuts import render
from ecrpg.models import  ManagementTeam, ManagementTeamlvl2, ManagementTeamlvl3, ManagementTeamHelper
# Create your views here.
def EcrpgIndex(request):

    return render(request, 'ecrpg.html')

def AdminTeam(request):

    lvl3 = ManagementTeamlvl3.objects.all()
    lvl2 = ManagementTeamlvl2.objects.all()
    lvl = ManagementTeam.objects.all()
    helper = ManagementTeamHelper.objects.all()

    context = {
        'admin3':lvl3,
        'admin2':lvl2,
        'admin':lvl,
        'helper':helper,
    }

    return render(request,'managementTeam.html', context)