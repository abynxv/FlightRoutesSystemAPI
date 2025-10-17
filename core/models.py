from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)

class Route(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()