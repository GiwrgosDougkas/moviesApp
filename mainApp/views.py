from itertools import zip_longest

from django.shortcuts import render

from mainApp.models import Movie


# Create your views here.

def post_list(request):
    renderSearch = True
    moviesAll = Movie.objects.all()
    movies = list(zip_longest(*[iter(moviesAll)]*4))

    return render(request, 'mainApp/movie_list.html', {'movies': movies, 'renderSearch': renderSearch})


def about_us(request):
    return render(request, 'mainApp/about_us.html')
