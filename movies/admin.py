from django.contrib import admin

# Register your models here.
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name"]

admin.site.register(Movie, MovieAdmin)
