from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h4>Hello, world. You're at the polls index.</h4>")

def about(request):
    return HttpResponse("<h4>This is the about page.</h4>")
