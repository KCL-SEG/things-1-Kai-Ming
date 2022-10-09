from django.db import models

# Create your models here.
class Thing:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __del__(self):
        print('A thing was deleted')

    def full_clean(self):
        del(self)