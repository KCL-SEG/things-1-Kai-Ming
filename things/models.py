from enum import unique
from pickle import FALSE
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

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
        validators = [
            MinLengthValidator(0),
            MaxLengthValidator(100),
        ]

    )       
