from django.shortcuts import render
from .models import Movie
from django.db.models import annotate, avg, count
# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # ratings = movie.ratings_set.all()

    return render(request,
                  'movies/movie_detail.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    rater = Movie.objects.get(pk=rater_id)
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
    for movie in Movie.objects.all():
        if type(movie.average_rating()) == float:
            movie_list.append(movie)
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
        .filter(num_ratings_gte=50)
    movies = Movie.objects.annotate(Avg('rating__stars')) \
        .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'movies/top_movies.html',
                  {})
