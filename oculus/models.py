from django.db import models


class Position(models.Model):
    w = models.CharField(max_length=128, null=True, blank=True)
    x = models.CharField(max_length=128, null=True, blank=True)
    y = models.CharField(max_length=128, null=True, blank=True)
    z = models.CharField(max_length=128, null=True, blank=True)
    time_received = models.DateField()
