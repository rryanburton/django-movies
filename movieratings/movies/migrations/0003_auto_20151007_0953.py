# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20151007_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(blank=True, max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
        ),
    ]
