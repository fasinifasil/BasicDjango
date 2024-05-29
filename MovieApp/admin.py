from django.contrib import admin

from MovieApp.models import MovieDb, Director,CensorInfo,Actor

# Register your models here.
admin.site.register(MovieDb)
admin.site.register(Director)
admin.site.register(CensorInfo)
admin.site.register(Actor)