from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review (models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(0, 'Review cannot be lower than 0 stars'),
                                MaxValueValidator(5, 'Review cannot be higher than 5 stars ')])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie.title
