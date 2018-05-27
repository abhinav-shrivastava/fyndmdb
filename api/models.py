from django.db import models

# Movie model
# Contains name, imdb score, genre, director and 99popularity of a movie

class Movie(models.Model):
  name = models.CharField(max_length=200)
  director =  models.CharField(max_length=200)
  imdb_score = models.DecimalField(max_digits=4, decimal_places=1)
  popularity = models.DecimalField(max_digits=4, decimal_places=1)
  genre = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '{} ({})'.format(self.name, self.imdb_score)
