from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def Service(request):
    return render(request, "service.html")

def About(request):
    return render(request, "about.html")