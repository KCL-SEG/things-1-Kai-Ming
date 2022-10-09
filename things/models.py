from django.db import models

# Create your models here.
class Thing:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    
    def __str__(self):
        return self.name