
from django.db import models

class Positions(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=2)
