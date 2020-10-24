from django.db import models
from locations.cities.models import City



class AdministrativeRegion(models.Model):
    name = models.CharField(
        max_length=255,
    )

    city = models.ForeignKey(
        City,
        null=True,
        on_delete=models.SET_NULL,
    )


    def __str__(self):
        return f'Admin..Region("{self.name}", "{self.city.name}")'
    

    class Meta:
        unique_together = (
            'name',
            'city',
        )