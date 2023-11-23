from django.contrib import admin
from django.contrib.admin import site

from . import models
from .models import movie_table

# Register your models here.
admin.site.register(movie_table)
