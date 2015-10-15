# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('occupation', models.IntegerField(max_length=2, choices=[(0, 'other'), (1, 'academic/educator'), (2, 'artist'), (3, 'clerical/admin'), (4, 'college/grad student'), (5, 'customer service'), (6, 'doctor/health care'), (7, 'executive/managerial'), (8, 'farmer'), (9, 'homemaker'), (10, 'K-12 student'), (11, 'lawyer'), (12, 'programmer'), (13, 'retired'), (14, 'sales/marketing'), (15, 'scientist'), (16, 'self-employed'), (17, 'technician/engineer'), (18, 'tradesman/craftsman'), (19, 'unemployed'), (20, 'writer')])),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('stars', models.IntegerField(max_length=1, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('movie', models.ForeignKey(to='movieapp.Movie')),
                ('rater', models.ForeignKey(to='movieapp.Rater')),
            ],
        ),
    ]
