from django.contrib import admin

from .models import movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'release')
    
admin.site.register(movie)
