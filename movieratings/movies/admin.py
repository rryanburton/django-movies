from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'occupation', 'zipcode']


# Register your models here.
admin.site.register(Rater)
