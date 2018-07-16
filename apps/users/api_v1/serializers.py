from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.users.models import User, UserState


class UserSerializer(serializers.ModelSerializer):

    idUser = serializers.IntegerField(read_only=True, source='id')
    password = serializers.CharField(write_only=True)
    sex = serializers.ChoiceField(choices=User.SEXO_CHOICES, write_only=True)

    class Meta:
        model = User
        fields = ('idUser', 'username', 'password', 'sex')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserState
        fields = ('message', 'user')
