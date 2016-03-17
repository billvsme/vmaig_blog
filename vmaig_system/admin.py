from django.contrib import admin
from vmaig_system.models import Notification

# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = ('title', 'from_user', 'to_user', 'create_time')
    list_filter = ('create_time',)
    fields = ('title', 'is_read', 'text', 'url', 'from_user', 'to_user')


admin.site.register(Notification, NotificationAdmin)
