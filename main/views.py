from django.shortcuts import render
from django.http import HttpResponse # This line is not needed

# Create your views here.
def index(request):
    data  = {
        'title': 'Main page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
