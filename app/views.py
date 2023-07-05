from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def ourTeam(request):
    return render(request,"our-team.html")