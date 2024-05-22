from django.db import models


NATIONALITY_COICE = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brazil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_COICE,
                                   blank=True, null=True)

    def __str__(self):
        return self.name
