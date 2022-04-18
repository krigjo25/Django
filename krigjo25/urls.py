from . import views
from django.urls import path

urlpatterns = [
                path('', views.webIndex, name = 'index'),
                path('<int:pk>/', views.ProjectDetail, name = 'detail'),
]