from django.db import models

# Create your models here.


class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),)

    OCCUPATION_CHOICES = (
        (0, "other"),
        (1, "academic/educator"),
        (2, "artist"),
        (3, "clerical/admin"),
        (4, "college/grad student"),
        (5, "customer service"),
        (6, "doctor/health care"),
        (7, "executive/managerial"),
        (8, "farmer"),
        (9, "homemaker"),
        (10, "K-12 student"),
        (11, "lawyer"),
        (12, "programmer"),
        (13, "retired"),
        (14, "sales/marketing"),
        (15, "scientist"),
        (16, "self-employed"),
        (17, "technician/engineer"),
        (18, "tradesman/craftsman"),
        (19, "unemployed"),
        (20, "writer"))

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.IntegerField(choices=OCCUPATION_CHOICES)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return "user #" + str(self.pk)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Rating(models.Model):
    STARS_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),)
    stars = models.IntegerField(choices=STARS_CHOICES)
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.rater.pk + self.movie.title + self.rating
