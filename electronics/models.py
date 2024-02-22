from django.db import models


class Mobile(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.name}"
