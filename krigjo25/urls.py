from . import views
from django.urls import path

urlpatterns = [
                path('', views.WebIndex, name = 'index'),
                path('blog/', views.BlogIndex, name = 'blogIndex'),
                path('<int:pk>/', views.BlogDetails, name = 'BlogDetail'),
                path('<category>/', views.BlogCategory, name = 'BlogCategory'),
                path('<int:pk>/', views.ProjectDetail, name = 'ProjectDetail'),
]