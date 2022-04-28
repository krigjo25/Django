from . import views
from django.urls import path

urlpatterns = [
                path('', views.EcRPGIndex, name = 'ecrpg'),
                path('wiki/', views.WikiIndex, name = 'ecrpgwiki'),
                path('rules/', views.CommunityRules, name = 'rules'),
                path('wiki/<int:pk>/', views.WikiDetails, name = 'WikiDetails'),
                path('wiki/<category>/', views.wikiPost, name = 'wikiPost'),
                path('management/', views.managementTeam, name = 'managementTeam'),

]