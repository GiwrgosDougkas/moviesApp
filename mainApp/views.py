from django.shortcuts import render

from mainApp.models import Movie


# Create your views here.

def post_list(request):
    movies = Movie.objects.all()
    return render(request, 'mainApp/post_list.html', {'movies':movies})

def about_us(request):
    return render(request, 'mainApp/about_us.html')