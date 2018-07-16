from django.contrib import admin

from apps.events.models import Event, Status, UserStatus, SleepHourStatus


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'created',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(SleepHourStatus)
class SleepHourStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_hour', 'max_hour', 'status')


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
