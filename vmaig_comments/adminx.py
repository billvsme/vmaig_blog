#coding:utf-8
from vmaig_comments.models import Comment

import xadmin


class CommentAdmin(object):
    search_fields = ('user__username','article__title','comment')
    list_filter = ('create_time',)
    list_display = ('user','article','create_time')
    fields = ('user','article','comment')

xadmin.site.register(Comment,CommentAdmin)



