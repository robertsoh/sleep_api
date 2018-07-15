from django.db import models

from apps.users.models import User


class EventType(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    TYPE_SLEEP = 'SLEEP'
    TYPE_AWAKE = 'AWAKE'
    TYPE_CHOICES = (
        (TYPE_SLEEP, 'Sleep'),
        (TYPE_AWAKE, 'Awake'),
    )

    user = models.ForeignKey(User, related_name='events')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
