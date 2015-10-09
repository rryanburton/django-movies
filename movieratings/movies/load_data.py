import csv
import json


ml_dir = '../ml-1m'


def load_rater_data():
    raters = []
    with open(ml_dir + '/users.dat') as f:
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

    with open('fixtures/raters.json', 'w') as f:
        f.write(json.dumps(raters))


def load_movie_data():
    movies = []
    with open(ml_dir + '/movies.dat', encoding='windows-1252') as f:
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

    with open('fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))


def load_ratings_data():
    ratings = []

    with open(ml_dir + '/ratings.dat') as f:
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

    with open('fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))


def load_all_data():
    load_rater_data()
    load_movie_data()
    load_ratings_data()

load_all_data()
