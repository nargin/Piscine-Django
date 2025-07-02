from django.http import HttpResponse
import psycopg2
import json

# Create your views here.

def init(request):
    try:
        conn = psycopg2.connect(
            dbname='piscine_django',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
        print("Connected to the database successfully.")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movie (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT NULL,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)
        cursor.execute("SELECT * FROM ex00_movie;")
        movies = cursor.fetchall()
        cursor.close()
        conn.close()
        # Return JSON response
        return HttpResponse(json.dumps({
            "success": "OK",
            "movies": movies
        }), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({
            "error": str(e)
        }), content_type='application/json', status=500)