from django.db import models
from django.contrib.auth.models import User
from foods.models import Food

class Meal(models.Model):
    MEAL_TYPE = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    meal_type = models.CharField(choices=MEAL_TYPE, default=MEAL_TYPE[3][0])
    foods = models.ManyToManyField(Food, through='MealFood')

