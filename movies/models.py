from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return str(self.id) + ' - ' + self.name
>>>>>>> f432ca7d3715af8939d7422eef82501ea855026b
