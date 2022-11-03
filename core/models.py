from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=250)
    metric=models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unit_of_measure = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name="records")
    date=models.DateField(auto_now_add=True)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return f"Record for {self.habit.name}"

class Date(models.Model):
    year = models.ForeignKey('Year', on_delete=models.CASCADE, blank=True, null=True, related_name='date')