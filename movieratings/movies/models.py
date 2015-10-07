from django.db import models


# Create your models here.


class Rater(models.Model):
    # id is automatic

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'Did not answer'),
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    occupation = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars_avg']

    def __str__(self):
        return self.title


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '@{} gives {} a {}*'.format(self.user, self.movie, self.stars)
