from django.conf.urls import url

from apps.events.api_v1.views import EventSleepAPIView, EventAwakeAPIView

urlpatterns = [
    url(r'^sleep$', EventSleepAPIView.as_view(), name='sleep_event'),
    url(r'^awake$', EventAwakeAPIView.as_view(), name='awake_event')
]