from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.events.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('type', 'user',)

    def validate(self, data):
        user = data.get('user')
        last_event = user.last_event()
        if last_event and last_event.type == data.get('type'):
            raise ValidationError('The user is already {}'.format(last_event.get_type_display()))
        return data
