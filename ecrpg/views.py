from django.shortcuts import render
from ecrpg.models import AdminTeam
# Create your views here.
def weECRPG(request):
    
    #   Initializing the database connection
    admin = AdminTeam.objects.all()
    context = {
                'AdminTeam': admin,
}

    return render(request, 'index.html', context)