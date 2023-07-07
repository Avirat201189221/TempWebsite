from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def ourTeam(request):
    return render(request,"our-team.html")

def events(request):
    return render(request,"events.html")

def colloquium(request):
    return render(request,"colloquium.html")

def hackonix(request):
    return render(request,"hackonix.html")

def qoc(request):
    return render(request,"qoc.html")