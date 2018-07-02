from django.urls import path, include
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('/createProject', views.create_project, name='create_project'),
    path('/saveProject', views.save_project, name='save_project')
]
