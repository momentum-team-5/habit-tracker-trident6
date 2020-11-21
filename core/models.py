from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=255)
    metric = models.CharField(max_length=255)
    target = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.metric} {self.target}"

class Record(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name='records')
    text = models.TextField(blank=True)
    completed = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["habit", "date"], name="unique_record")
        ]

    def __str__(self):
        return f"{self.habit} {self.date}"
