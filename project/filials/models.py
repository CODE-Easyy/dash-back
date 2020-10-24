from django.db import models

from locations.cities.models import City
from accounts.models import Profile

from .validators import validate_coordinates

class Filial(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    city = models.ForeignKey(
        City,
        null=True,
        on_delete=models.SET_NULL,
    )

    actual_address = models.CharField(
        max_length=255,
    )

    legal_address = models.CharField(
        max_length=255,
    )

    coordinates = models.CharField(
        max_length=100,
        validators=[
            validate_coordinates,
        ]
    )


    contact_persons  = models.ManyToManyField(
        Profile,
    )



    def __str__(self):
        return f'Filial("{self.name}", "{self.city.name}")'

    

