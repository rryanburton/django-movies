from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'occupation', 'zipcode']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movietitle']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating']

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)
