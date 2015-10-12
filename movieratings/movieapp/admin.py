from django.contrib import admin
# from django.conf.urls.defaults import *
from .models import Rater, Movie


# urlpatterns = patterns('',
#                        (r'^admin/', include('django.contrib.admin.urls')),
#                        )


class RaterAdmin(admin.ModelAdmin):
    list_display = ['pk', 'age', 'gender', 'occupation', 'zipcode']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_rating']

# Register your models here.

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
