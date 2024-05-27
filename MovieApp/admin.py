from django.contrib import admin

from MovieApp.models import MovieDb, Director

# Register your models here.
admin.site.register(MovieDb)
admin.site.register(Director)