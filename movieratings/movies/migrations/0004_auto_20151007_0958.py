# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20151007_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
