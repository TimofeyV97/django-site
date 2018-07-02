from django.urls import path, include
from . import views

app_name = 'edit'
urlpatterns = [
    path('editPhases', views.edit_phases, name='edit_phases'),
    path('editPhase', views.edit_phase, name='edit_phase'),
    path('editPhases2', views.save_edit_phase, name='save_edit_phase'),
    path('editProjects', views.edit_projects, name='edit_projects'),
    path('editProject', views.edit_project, name='edit_project'),
    path('editProjects2', views.save_edit_project, name='save_edit_project'),
    path('editProjects3', views.edit_projects_manager, name='edit_projects_manager'),
    path('editProject2', views.edit_project_manager, name='edit_project_manager'),
    path('editProjects4', views.save_edit_project_manager, name='save_edit_project_manager'),
    path('editUsers', views.edit_users, name='edit_users'),
    path('editUser', views.edit_user, name='edit_user'),
    path('editUser2', views.save_edit_user, name='save_edit_user'),
    path('editProjects5', views.delete_project, name='delete_project'),
]
