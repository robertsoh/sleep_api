from datetime import datetime

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
    sleep_hour = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id and self.type == self.TYPE_AWAKE:
            self.compute_sleep_hours()
        super().save(*args, **kwargs)

    def compute_sleep_hours(self):
        last_event = Event.objects.filter(user=self.user).last()
        if last_event:
            diff_seconds = datetime.now() - last_event.created
            self.sleep_hour = int(diff_seconds.total_seconds() / 3600)


class Status(models.Model):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.name


class SleepHourStatus(models.Model):
    min_hour = models.IntegerField('Hora mínima')
    max_hour = models.IntegerField('Hora máxima')
    status = models.ForeignKey(Status, related_name='+')


class UserStatus(models.Model):
    user = models.ForeignKey(User, related_name='status')
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.status.name)
