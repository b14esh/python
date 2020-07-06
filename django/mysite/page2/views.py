from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'page2/index.html')

# в папке static/page2 - лежат картинки
# в папке template/page2 лежит index.html