from enum import unique
from pickle import FALSE
from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique = True,
        blank = True,
    )
    description = models.CharField(
        max_length=120,
        blank = False,
        unique = False,
    )
    quantity = models.IntegerField(
        min_value=0,
        max_value=100,

    )       
