from django.db import models

# Create your models here.
class Pizza(models.Model):
    '''voici une pizza'''
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        '''retourne le nom de la pizza'''
        return self.name

class Topping(models.Model):
    pizza = models.ManyToManyField(Pizza)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
