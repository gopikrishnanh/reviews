from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.


def home(request):
    cat = categ.objects.all()
    categ_name=request.GET.get("categories")
    if categ_name !=None:
        mov = Movie.objects.filter(category=categ_name)
    else:
         mov = Movie.objects.all()

    return render(request, 'index.html', {'mv': mov, 'ct': cat})


def details(request, Movie_id):
    deta = Movie.objects.get(id=Movie_id)
    return render(request, 'details1.html', {'mo': deta})


def search(request):
    q = request.GET['q']
    mov = Movie.objects.filter(name__contains=q)
    return render(request, 'search.html', {'mv': mov})
