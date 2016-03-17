# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from blog.models import Article

# Create your models here.


# 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,所以修改str类的title方法就可以实现.
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'用户')
    article = models.ForeignKey(Article, verbose_name=u'文章')
    text = models.TextField(verbose_name=u'评论内容')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    parent = models.ForeignKey('self', default=None, blank=True, null=True,
                               verbose_name=u'引用')

    class Meta:
        verbose_name_plural = verbose_name = u'评论'
        ordering = ['-create_time']
        app_label = string_with_title('vmaig_comments', u"评论管理")

    def __unicode__(self):
        return self.article.title + '_' + str(self.pk)

    __str__ = __unicode__
