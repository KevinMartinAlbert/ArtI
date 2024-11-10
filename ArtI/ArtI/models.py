from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Creator(models.Model):

    name = models.CharField(max_length=100)
    biography = models.CharField(max_length=10000)
    release_year = models.IntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(9999)]
    )
    official_homepage = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Creation(models.Model):

    title = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    creation_date = models.IntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(9999)], null=True
    )
    creator = models.ForeignKey(Creator, null=True, on_delete=models.SET_NULL)
