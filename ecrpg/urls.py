from . import views
from django.urls import path

urlpatterns = [
                path('', views.EcrpgIndex, name = 'ecrpg'),
                path('wiki/', views.GameWiki, name = 'gameWiki'),
                path('rules/', views.CommunityRules, name = 'rules'),
                path('management/', views.AdminTeam, name = 'managementTeam'),

]