
from django.urls import path
from . import views

urlpatterns = [
    path("", views.project, name='allProjects'),
    path("add/", views.add_project, name='add_Project'),

    path("<int:id>/", views.delete_project, name="delete_project"),


]