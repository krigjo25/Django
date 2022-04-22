from . import views
from django.urls import path

urlpatterns = [
                path('', views.EcrpgIndex, name = 'ecrpg'),
                path('management/', views.AdminTeam, name = 'managementTeam'),

]