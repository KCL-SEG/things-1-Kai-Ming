from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    request = HttpResponse('<html>Things</html><h1>Things</h1>')
    return response
    #return render(request, 'home.html')
