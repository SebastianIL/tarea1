from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('<h1> Bienvenidos a la sesión del jueves! </h1>')
    return render(request,'index.html')