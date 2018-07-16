from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_v1.serializers import UserSerializer, UserStateSerializer
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
        last_state = user.last_state()
        status = last_status.status
        data = {
            'status': status.id if status else None,
            'status_label': status.name if status else None,
            'sleep_hour': last_event.sleep_time() if last_event else None,
            'message': last_state.message if last_state else ''
        }
        return Response(data, status=200)


class UserStateCreateAPIView(CreateAPIView):
    serializer_class = UserStateSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        data.update({
            'user': self.request.user.id
        })
        return super().post(request, *args, **kwargs)
