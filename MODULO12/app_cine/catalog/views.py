from django.shortcuts import render

# Create your views here.

from .models import Director,Pelicula

def index(request):
    num_pelis = Pelicula.objects.all().count()
    num_directores = Director.objects.all().count()

    pelis_terror = Pelicula.objects.filter(status__exact='t'.count())
    return render(
        request,
        'index.html',
        context={
            'num_pelis':num_pelis,
            'num_directores':num_directores
        }
    )
