from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'occupation', 'zipcode']


class Movie(models.Model):
    list_display = ['movietitle']


class Rating(models.Model):
    list_display = ['userid', 'movieid', 'rating']

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)
