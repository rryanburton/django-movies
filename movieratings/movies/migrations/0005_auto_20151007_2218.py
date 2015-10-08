# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20151007_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movietitle',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.PositiveIntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]
