from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_v1.serializers import UserSerializer
from apps.users.models import User


class UsersCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class SearchUserListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            qs = User.objects.filter(username__icontains=username)
        else:
            qs = User.objects.none()
        return qs


class InitDataView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        last_status = user.last_status()
        last_event = user.last_event()
        status = last_status.status
        data = {
            'status': status.id if status else None,
            'status_label': status.name if status else None,
            'sleep_hour': last_event.sleep_hour if last_event else None
        }
        return Response(data, status=200)
