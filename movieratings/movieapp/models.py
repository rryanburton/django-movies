from django.db import models

# Create your models here.


class Rater(models.Model):
    # id is automatic
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
    occupation = models.CharField(max_length=2, choices=OCCUPATION_CHOICES)
    zipcode = models.CharField(max_length=5)


class Movie(models.Model):
    pass


class Rating(models.Model):
    pass
