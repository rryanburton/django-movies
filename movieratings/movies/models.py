from django.db import models

# Create your models here.


class Rater(models.Model):
    # id is automatic

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'Did not answer'),
    )
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return '{}'.format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return self.title


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '@{} gives {} a {}*'.format(self.rater, self.movie, self.stars)


def load_rater_data():
    import csv
    import json
    raters = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
            delimiter='\t')
        for row in reader:
            rater = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'movies.Rater',
                'pk': int(row['UserID']),
            }
            raters.append(rater)

    with open('raters.json', 'w') as f:
        f.write(json.dumps(raters))


def load_movie_data():
    import csv
    import json
    movies = []
    with open('ml-1m/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='MovieID::Title::Genres'.split('::'),
            delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'movies.Movie',
                'pk': int(row['MovieID']),
            }
            movies.append(movie)

    with open('movies.json', 'w') as f:
        f.write(json.dumps(movies))


def load_ratings_data():
    import csv
    import json

    ratings = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
            delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'rater': row['UserID'],
                    'movie': row['MovieID'],
                    'stars': row['Rating'],
                },
                'model': 'movies.Rating',
            }
            ratings.append(rating)

    with open('ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
