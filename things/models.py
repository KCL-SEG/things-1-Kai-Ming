from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

# Create your models here.

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique = True,
        blank = False,
    )
    description = models.CharField(
        max_length=120,
        blank = True,

        unique = False,
    )
    quantity = models.IntegerField(
        unique = False,
        validators = [
            MaxLengthValidator(100),
            MinLengthValidator(0),
        ]

    )       
