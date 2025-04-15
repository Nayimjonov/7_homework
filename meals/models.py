from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')