from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movie, Rater

# Create your views here.


def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'movieapp/movie_details.html',
                  {'movie': movie})


def rater_details(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all
    movie_ratings = []
    for rating in ratings():
        movie_ratings.append({
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars,
        })

    # average = sum(rating.stars) / len(rating.stars)
    return render(request,
                  'movieapp/rater_details.html',
                  {'rater': rater,
                   #    'average rating': average,
                   'movie_ratings': movie_ratings})


def top_movies(request):
    popular_movies = Movie.objects.all().annotate(num_ratings=Count('rating')) \
        .filter(num_ratings__gte=25)
    top_mov = popular_movies.annotate(Avg('rating__stars'))
    top_20_mov = top_mov.order_by('-rating__stars__avg')[:20]

    return render(request,
                  'movieapp/top_movies.html',
                  {'movies': top_20_mov})


def most_reviewed(request):
    popular_movies = Movie.objects.all().annotate(num_ratings=Count('rating'))
    most_rev = popular_movies.order_by('-num_ratings')[:20]
    return render(request,
                  'movieapp/most_rev.html',
                  {'most_reviewed': most_rev})


def all_movies(request):
    Movie.objects.all()
