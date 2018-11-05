from django.conf.urls import url
from rest_framework.authtoken import views

from apps.users.api_v1.views import UsersCreateAPIView, SearchUserListView, InitDataView, UserStateCreateAPIView

urlpatterns = [
    url(r'^register$', UsersCreateAPIView.as_view(), name='register_user'),
    url(r'^login$', views.obtain_auth_token, name='login'),
    url(r'^searchUsers$', SearchUserListView.as_view(), name='search_user'),
    url(r'^initData$', InitDataView.as_view(), name='init_data'),
    url(r'^registerState$', UserStateCreateAPIView.as_view(), name='register_state')
]