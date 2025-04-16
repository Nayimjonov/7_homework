from django.db import models
from django.conf import settings
from foods.models import Food

class Meal(models.Model):
    MEAL_TYPE = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),

    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    meal_type = models.CharField(choices=MEAL_TYPE, default=MEAL_TYPE[3][0])
    foods = models.ManyToManyField(Food, through='MealFood')

    def __str__(self):
        return f"{self.get_meal_type_display()} by {self.user.username} on {self.date}"

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_foods')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='meal_foods')
    quantity = models.DecimalField(max_digits=5, decimal_places=2),


    def __str__(self):
        return f"{self.quantity}g of {self.food.name} in {self.meal}"