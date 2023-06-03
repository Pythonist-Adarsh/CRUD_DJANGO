from statistics import mode
from django.db import models

#model
class Customerr(models.Model):
    #id=models.Integerfield(max_length=20)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    number=models.IntegerField()
    def __str__(self):
        return self.name
    
