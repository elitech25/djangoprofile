from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("allProjects")
    else:
        form = UserCreationForm()
    return render(request, "user/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return redirect("allProjects")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {"form":form})


#! user logout from the account
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("user_login")