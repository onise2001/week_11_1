from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, "main/home.html")

def aboutpage(request):
    return render(request, "main/about.html")

def contactpage(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        #return HttpResponse("HEllo")

        return render(request, "main/hello.html", {"first_name": first_name, "last_name": last_name})
    
    #return HttpResponse("contact")
    return render(request, "main/contact.html")