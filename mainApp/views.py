from itertools import zip_longest

from django.shortcuts import render, get_object_or_404

from mainApp.models import Movie


# Create your views here.

def post_list(request):
    renderSearch = True
    moviesAll = Movie.objects.all();
    moviesYear = list(zip_longest(*[iter(moviesAll.order_by("-year"))]*4))
    moviesRating = list(zip_longest(*[iter(moviesAll.order_by("-rating"))]*4))

    return render(request, 'mainApp/movie_list.html', {'movies_all': moviesAll.order_by("-title"), 'movies_year': moviesYear, 'renderSearch': renderSearch, 'movies_rating': moviesRating})


def about_us(request):
    return render(request, 'mainApp/about_us.html')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'mainApp/movie_detail.html', {'movie':movie});