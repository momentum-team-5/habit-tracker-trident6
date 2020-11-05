from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# class User(models.Model):
#     name = models.CharField(max_length=255)


class Habit(models.Model):
    name = models.CharField(max_length=255)
    target = models.IntegerField(blank=True, null=True)


class record(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    completed = models.IntegerField(blank=True, null=True)
    entry_date = models.DateField(auto_now=True)