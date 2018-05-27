import json
from django.db import models

# Movie model
# Contains name, imdb score, genre, director and 99popularity of a movie

class Movie(models.Model):
  name = models.CharField(max_length=200, unique=True)
  director =  models.CharField(max_length=200)
  imdb_score = models.DecimalField(max_digits=4, decimal_places=1)
  popularity = models.DecimalField(max_digits=4, decimal_places=1)
  genre = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  # We serialize the genre field, unless it's null before adding it to the DB.
  def save(self):
    self.genre = json.dumps(self.genre) if self.genre else json.dumps([])
    super(Movie, self).save()

  def __str__(self):
    return '{} ({})'.format(self.name, self.imdb_score)
