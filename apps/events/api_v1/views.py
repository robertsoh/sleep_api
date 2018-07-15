from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.events.api_v1.serializers import EventSerializer
from apps.events.models import Event


class EventSleepAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.id,
            'type': Event.TYPE_SLEEP
        }
        serializer = EventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('OK', status=201)


class EventAwakeAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.id,
            'type': Event.TYPE_AWAKE
        }
        serializer = EventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('OK', status=201)
