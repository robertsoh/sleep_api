from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SEXO_FEMENINO = 'F'
    SEXO_MASCULINO = 'M'
    SEXO_CHOICES = (
        (SEXO_FEMENINO, 'Femenino'),
        (SEXO_MASCULINO, 'Masculino')
    )
    sex = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    username = models.CharField('Username', max_length=50, unique=True)

    def last_event(self):
        return self.events.last()

    def last_status(self):
        return self.status.last()

    def last_state(self):
        return self.states.last()


class UserState(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='states')

    def __str__(self):
        return '{}: {}'.format(self.user, self.message)
