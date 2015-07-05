#coding:utf-8
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.admin import UserAdmin
from vmaig_auth.models import VmaigUser
from vmaig_auth.forms import VmaigUserCreationForm

import xadmin
from reversion.models import Revision

# Register your models here.

"""
class VmaigUserAdmin(UserAdmin):
    add_form = VmaigUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email' , 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (u'基本信息', {'fields': ('username', 'password','email')}),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )
"""

xadmin.site.unregister(Group)
xadmin.site.unregister(Permission)
