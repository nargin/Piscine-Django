from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.

def populate(request):
    movies_data = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kutz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]

    results = []
    for movie_data in movies_data:
        try:
            Movies.objects.create(**movie_data)
            results.append(f"OK: {movie_data['title']} added.")
        except Exception as e:
            results.append(f"Error adding {movie_data['title']}: {e}")

    return HttpResponse("<br>".join(results))

def display(request):
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available")

    table = "<table border='1'><tr><th>Episode Number</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
    for movie in movies:
        table += f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td></tr>"
    table += "</table>"
    return HttpResponse(table)
