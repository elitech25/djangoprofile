from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "Elai-tech.html")

def contact(request):
    return render(request, "contact.html")

