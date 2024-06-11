from django.db import models

# Create your models here.
from django.conf import settings


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="low",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        limit_choices_to={"is_superuser": False},
        related_name="tasks",
        null=True,
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
