from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name"]

admin.site.register(Movie, MovieAdmin)
>>>>>>> f432ca7d3715af8939d7422eef82501ea855026b
