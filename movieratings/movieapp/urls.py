from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail, name='movie_detail'),
    url(r'rater/(?P<rater_id>\d+)$', views.rater_detail, name='rater_detail'),
    url(r'top', views.top_movies, name='top_movies'),
    url(r'most', views.most_reviewed, name='most_rev'),
]
