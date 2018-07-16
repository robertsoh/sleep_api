from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.events.api_v1.serializers import EventSerializer
from apps.events.models import Event, UserStatus, SleepHourStatus, Status


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
        event = serializer.save()
        user_status = self.create_user_status(event)
        data_response = {
            'status': user_status.status_id,
            'status_label': user_status.status.name
        }
        return Response(data_response, status=201)

    def create_user_status(self, event):
        status = Status.objects.get(id=8)
        return UserStatus.objects.create(user=event.user, status=status)


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
        event = serializer.save()
        user_status = self.create_user_status(event)
        data_response = {
            'status': user_status.status_id,
            'status_label': user_status.status.name,
            'sleep_hour': event.sleep_hour
        }
        return Response(data_response, status=201)

    def create_user_status(self, event):
        sleep_hour_status = SleepHourStatus.objects.filter(min_hour__gte=event.sleep_hour,
                                                           max_hour__lte=event.sleep_hour).first()
        return UserStatus.objects.create(user=event.user, status=sleep_hour_status.status)
