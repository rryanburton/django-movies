from django.shortcuts import render
from django.db.models import Avg, Count

from .models import Movie, Rater


# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'movies/movie_detail.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars,
        })
    return render(request,
                  'movies/rater_detail.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})


def top_movies(request):
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
        .filter(num_ratings__gte=50)
    movies = popular_movies.annotate(Avg('rating__stars')) \
        .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'movies/top_movies.html',
                  {'movies': movies})
