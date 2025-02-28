from django.shortcuts import render
from django.http import HttpResponse # This line is not needed

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
