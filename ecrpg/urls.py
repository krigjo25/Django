from . import views
from django.urls import path

urlpatterns = [
                path('/ecrpg/', views.webEcrpg, name = 'index'),

]