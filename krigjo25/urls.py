from . import views
from django.urls import path

urlpatterns = [
                path('', views.webIndex, name = 'index'),
                path('test/bg/', views.TestBackGround, name = 'Backgrounds'),
                path('<int:pk>/', views.ProjectDetail, name = 'detail'),
]