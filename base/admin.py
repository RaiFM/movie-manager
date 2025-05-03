from django.contrib import admin

from .models import movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release', 'genre')
    
admin.site.register(movie, MovieAdmin)
