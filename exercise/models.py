from django.db import models


class Exercise(models.Model):
    CHOICES_CATEGORY = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CHOICES_CATEGORY, default=CHOICES_CATEGORY[0][0])
    calories_burned_per_hour = models.PositiveIntegerField()

    def __str__(self):
        return self.name
