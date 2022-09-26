from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from MovieDatabase.models import MovieNames


def home(request):
    return render(request, "home.html")

def view(request):
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name', None)
        try:
            movie = MovieNames.objects.filter(movie_name=movie_name)
            return render(request, "view.html", {"movies": movie})
        except MovieNames.DoesNotExist:
            return HttpResponse(f"Error")

    return render(request, "view.html")




def insert(request):
    if request.method == "POST":
        movie_name = request.POST.get('mname', None)
        actor_name = request.POST.get('aname', None)
        actress_name = request.POST.get('atname', None)
        release_year = request.POST.get('mdate', None)
        director_name = request.POST.get('dname', None)

        MovieNames.objects.create(movie_name = movie_name, actor_name=actor_name, actress_name=actress_name,
                                  release_year=release_year, director_name=director_name)
        return HttpResponse(f"Data Inserted Successfully")

    return render(request, "insert.html")