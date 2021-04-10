from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"app2html.html")

def vishwa(request,data):
    return HttpResponse(f'<h1>welcome to webpage{data}</h1>')
