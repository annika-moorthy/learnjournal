from django.db import models


class Resources(models.Model):
    name = models.CharField(max_length=200)
    description_name = models.CharField(max_length=200)
    url = models.URLField()

