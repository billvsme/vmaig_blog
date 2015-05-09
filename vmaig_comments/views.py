#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from vmaig_comments.models import Comment
import logging

#logger
logger = logging.getLogger(__name__)


#设置Article model
from blog.models import Article
ArticleModel = Article

# Create your views here.

class CommentControl(View):
    def post(self, request, *args, **kwargs):
        #获取当前用户
        user = self.request.user
        #获取评论
        comment = self.request.POST.get("comment","")
        #判断当前用户是否是活动的用户
        if not user.is_authenticated():
            logger.error(u'[CommentControl]当前用户非活动用户:[%s]' % user.username)
            return HttpResponse(u"请登陆！",status=403)
        if not comment:
            logger.error(u'[CommentControl]当前用户输入空评论:[%s]' % user.username)
            return HttpResponse(u"请输入评论内容！",status=403)

        en_title = self.kwargs.get('slug','')
        try:
            #默认使用pk来索引(也可根据需要使用title,en_title在索引
            article = ArticleModel.objects.get(en_title=en_title)
        except ArticleModel.DoesNotExist:
            logger.error(u'[CommentControl]此文章不存在:[%s]' % en_title)
            raise PermissionDenied

        #保存评论
        comment = Comment.objects.create(
                user=user,
                article = article,
                comment = comment,
                )

        try:
            img = comment.user.img
        except Exception as e:
            img = "http://vmaig.qiniudn.com/image/tx/tx-default.jpg"

        #返回当前评论
        html = "<li>\
                    <div class=\"vmaig-comment-tx\">\
                        <img src="+img+" width=\"40\"></img>\
                    </div>\
                    <div class=\"vmaig-comment-content\">\
                        <a><h1>"+comment.user.username+"</h1></a>"\
                        +u"<p>评论："+comment.comment+"</p>"+\
                        "<p>"+comment.create_time.strftime("%Y-%m-%d %H:%I:%S")+"</p>\
                    </div>\
                </li>"

        return HttpResponse(html)
