from django.db import models


class Shirt(models.Model):
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f"{self.brand} {self.type}"
