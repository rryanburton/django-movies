from django.db import models


# Create your models here.


class Rater(models.Model):
    userid = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.IntegerField()
    zipcode = models.CharField(max_length=10)


class Movie(models.Model):
    movieid = models.IntegerField()
    movietitle = models.CharField(max_length=100)


class Rating(models.Model):
    userid = models.ForeignKey(Rater)
    movieid = models.ForeignKey(Movie)
    rating = models.IntegerField()
