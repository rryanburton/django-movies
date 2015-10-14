import csv
import json
from faker import Faker
from django.conf import settings


# from django.contrib.auth.models import User

# settings.configure()


raters_source = '../ml-1m/users.dat'
ratings_source = '../ml-1m/ratings.dat'
movies_source = '../ml-1m/movies.dat'

raters_fixture = 'fixtures/raters.json'
ratings_fixture = 'fixtures/ratings.json'
movies_fixture = 'fixtures/movies.json'


def main():
    settings.configure()

    load_all_data()


def load_all_data():

    print("\nloading {}".format(raters_source))
    load_raters_data()
    print("{} is ready!\n".format(raters_fixture))

    print("loading {}".format(movies_source))
    load_movies_data()
    print("{} is ready!\n".format(movies_fixture))

    print("loading {}".format(ratings_source))
    load_ratings_data()
    print("{} is ready!\n".format(ratings_fixture))


def load_raters_data():
    from django.contrib.auth.models import User
    User.objects.all().delete()
    count = 1
    fake = Faker()
    raters = []
    with open(raters_source) as f:
        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
            delimiter='\t')
        user_set = {fake.user_name() for _ in range(8000)}
        user_list = [x for x in user_set]
        for row in reader:
            # print('Reading row: {}'.format(count))
            auth_user = User(username=user_list[count],
                             email=fake.email(),
                             password='password',
                             pk=row['UserID'])
            rater = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'movieapp.Rater',
                'pk': auth_user.pk,
            }
            raters.append(rater)
            auth_user.save()
            count += 1

    with open(raters_fixture, 'w') as f:
        f.write(json.dumps(raters))


def load_ratings_data():
    ratings = []
    with open(ratings_source) as f:
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
                'model': 'movieapp.Rating',
            }
            ratings.append(rating)

    with open(ratings_fixture, 'w') as f:
        f.write(json.dumps(ratings))


def load_movies_data():
    movies = []
    with open(movies_source, encoding='windows-1252') as f:
        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='MovieID::Title::Genres'.split('::'),
            delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'movieapp.Movie',
                'pk': int(row['MovieID']),
            }
            movies.append(movie)

    with open(movies_fixture, 'w') as f:
        f.write(json.dumps(movies))


if __name__ == '__main__':
    main()
