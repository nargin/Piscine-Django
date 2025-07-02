from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.db import connection

def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex02_movies (
                    episode_nb INTEGER PRIMARY KEY,
                    title VARCHAR(64) UNIQUE NOT NULL,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                );
            """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def populate(request):
    movies_data = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "1999-05-19"},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2002-05-16"},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2005-05-19"},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kutz, Rick McCallum", "release_date": "1980-05-17"},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"},
    ]
    
    results = []
    for data in movies_data:
        try:
            movie, created = Movie.objects.update_or_create(
                episode_nb=data["episode_nb"],
                defaults={
                    "title": data["title"],
                    "director": data["director"],
                    "producer": data["producer"],
                    "release_date": data["release_date"],
                    "opening_crawl": data.get("opening_crawl", None)
                }
            )
            if created:
                results.append(f"OK: {movie.title} inserted.")
            else:
                results.append(f"OK: {movie.title} updated.")
        except Exception as e:
            results.append(f"Error for {data['title']}: {e}")
    
    return HttpResponse("<br>".join(results))

def display(request):
    try:
        movies = Movie.objects.all().order_by('episode_nb')
        if not movies:
            return HttpResponse("No data available")
        
        html_table = """
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
        <table>
            <thead>
                <tr>
                    <th>Episode Number</th>
                    <th>Title</th>
                    <th>Opening Crawl</th>
                    <th>Director</th>
                    <th>Producer</th>
                    <th>Release Date</th>
                </tr>
            </thead>
            <tbody>
        """
        for movie in movies:
            html_table += f"""
            <tr>
                <td>{movie.episode_nb}</td>
                <td>{movie.title}</td>
                <td>{movie.opening_crawl if movie.opening_crawl else 'NULL'}</td>
                <td>{movie.director}</td>
                <td>{movie.producer}</td>
                <td>{movie.release_date}</td>
            </tr>
            """
        html_table += """
            </tbody>
        </table>
        """
        return HttpResponse(html_table)
    except Exception as e:
        return HttpResponse(f"No data available: {e}")