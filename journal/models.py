from django.db import models


TOPIC_CHOICES = [
    ('testing', 'Testing'),
    ('developing', 'Testing'),
    ('databases', 'Database'),
    ('project management', 'Project Management'),
]


class Resources(models.Model):
    name = models.CharField(max_length=200)
    description_name = models.CharField(max_length=200)
    url = models.URLField()
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES, default="other")
