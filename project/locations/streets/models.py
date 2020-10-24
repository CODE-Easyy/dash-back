from django.db import models
from locations.cities.models import City


class Street(models.Model):
    name = models.CharField(
        max_length=255,
    )

    city = models.ForeignKey(
        City,
        null=True,
        on_delete=models.SET_NULL,
    )

    

    class Meta:
        unique_together = (
            'name', 
            'city',
        )