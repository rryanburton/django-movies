from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'occupation', 'zipcode']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_rating']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'stars', 'rater']

# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
