from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)

