from django.db import models

class Filme(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=200)

    def __str__(self):
        # ID. TITULO
        return f'{self.title}'




