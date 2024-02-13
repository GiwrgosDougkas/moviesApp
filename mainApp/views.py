from itertools import zip_longest

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from mainApp.models import Movie, Category


# Create your views here.

def post_list(request):
    renderSearch = True
    isSearching = False;
    moviesAll = Movie.objects.all().order_by("-title");
    parameters = ['all', 'category', 'title', 'year']
    getRequest = request.GET;
    param_name = ''
    if(len(getRequest) > 0):
        for param in parameters:
            if request.GET.__contains__(param):
                isSearching = True
                param_name = param
                param_value = request.GET.get(param_name)
                break

    if param_name == 'all':
        moviesAll = moviesAll.filter(Q(title__contains=param_value) | Q(summary__contains=param_name))
    elif param_name == 'title':
        moviesAll = moviesAll.filter(title__contains=param_value)
    elif param_name == 'category':
        moviesAll = moviesAll.filter(category__category=param_value)
    elif param_name == 'year':
        moviesAll = moviesAll.filter(year__year=param_value)

    categories = Category.objects.all()
    moviesYear = list(zip_longest(*[iter(moviesAll.order_by("-year"))]*4))
    moviesRating = list(zip_longest(*[iter(moviesAll.order_by("-rating"))]*4))

    return render(request, 'mainApp/movie_list.html', {'movies_all': moviesAll, 'movies_year': moviesYear, 'renderSearch': renderSearch, 'movies_rating': moviesRating, 'categories': categories, 'isSearching': isSearching})


def about_us(request):
    return render(request, 'mainApp/about_us.html')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'mainApp/movie_detail.html', {'movie':movie});