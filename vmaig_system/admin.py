from django.contrib import admin
from vmaig_system.models import Notification, Link

# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = ('title', 'from_user', 'to_user', 'create_time')
    list_filter = ('create_time',)
    fields = ('title', 'is_read', 'text',
              'url', 'from_user', 'to_user', 'type')


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'url')
    list_filter = ('create_time',)
    fields = ('title', 'url', 'type')


admin.site.register(Notification, NotificationAdmin)
admin.site.register(Link, LinkAdmin)
