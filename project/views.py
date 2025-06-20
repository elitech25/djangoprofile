from django.shortcuts import render, redirect
from .forms import AddNewProject
from .models import projectFormat
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="user_login")
def project(request):
    all_projects = projectFormat.objects.all
    return render(request, "projects/projects.html", {"all_projects": all_projects})

def add_project(request):
    if request.method == "POST":
        form = AddNewProject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allProjects")
    else:
         form = AddNewProject()
    return render(request, "projects/add.html", {"form" : form})


def delete_project(request, id):
    oneproject = projectFormat.objects.get(pk = id)
    if request.method == "POST":
        oneproject.delete()
        return redirect("allproject")
