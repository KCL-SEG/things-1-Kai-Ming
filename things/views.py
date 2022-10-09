#from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #response = HttpResponse('<html>Things</html>')
    #return response
    return render(request, 'templates/home.html')
