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
        # (X, 'Did not answer'),
    )
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=5)

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


def load_ml_data():
    import csv
    import json
    users = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
            delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'movies.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)
        with open('users.json', 'w') as f:
            f.write(json.dumps(users))
