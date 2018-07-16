from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

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
