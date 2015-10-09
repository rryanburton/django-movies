# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('movietitle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='rater',
            name='userid',
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, blank=True),
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(to='movies.Rater'),
        ),
    ]
