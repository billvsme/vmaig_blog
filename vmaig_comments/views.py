# -*- coding: utf-8 -*-
import logging
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from vmaig_comments.models import Comment
from vmaig_system.models import Notification
from blog.models import Article

ArticleModel = Article
# logger
logger = logging.getLogger(__name__)


# Create your views here.

class CommentControl(View):
    def post(self, request, *args, **kwargs):
        # 获取当前用户
        user = self.request.user
        # 获取评论
        text = self.request.POST.get("comment", "")
        # 判断当前用户是否是活动的用户
        if not user.is_authenticated():
            logger.error(
                u'[CommentControl]当前用户非活动用户:[{}]'.format(
                    user.username
                )
            )
            return HttpResponse(u"请登陆！", status=403)

        en_title = self.kwargs.get('slug', '')
        try:
            # 默认使用pk来索引(也可根据需要使用title,en_title在索引
            article = ArticleModel.objects.get(en_title=en_title)
        except ArticleModel.DoesNotExist:
            logger.error(u'[CommentControl]此文章不存在:[%s]' % en_title)
            raise PermissionDenied

        # 保存评论
        parent = None
        if text.startswith('@['):
            import ast
            parent_str = text[1:text.find(':')]
            parent_id = ast.literal_eval(parent_str)[1]
            text = text[text.find(':')+2:]
            try:
                parent = Comment.objects.get(pk=parent_id)
                info = u'{}回复了你在 {} 的评论'.format(
                    user.username,
                    parent.article.title
                )
                Notification.objects.create(
                    title=info,
                    text=text,
                    from_user=user,
                    to_user=parent.user,
                    url='/article/'+en_title+'.html'
                )
            except Comment.DoesNotExist:
                logger.error(u'[CommentControl]评论引用错误:%s' % parent_str)
                return HttpResponse(u"请勿修改评论代码！", status=403)

        if not text:
            logger.error(
                u'[CommentControl]当前用户输入空评论:[{}]'.format(
                    user.username
                )
            )
            return HttpResponse(u"请输入评论内容！", status=403)

        comment = Comment.objects.create(
                user=user,
                article=article,
                text=text,
                parent=parent
                )

        try:
            img = comment.user.img
        except Exception as e:
            img = "http://vmaig.qiniudn.com/image/tx/tx-default.jpg"

        print_comment = u"<p>评论：{}</p>".format(text)
        if parent:
            print_comment = u"<div class=\"comment-quote\">\
                                  <p>\
                                      <a>@{}</a>\
                                      {}\
                                  </p>\
                              </div>".format(
                                  parent.user.username,
                                  parent.text
                              ) + print_comment
        # 返回当前评论
        html = u"<li>\
                    <div class=\"vmaig-comment-tx\">\
                        <img src={} width=\"40\"></img>\
                    </div>\
                    <div class=\"vmaig-comment-content\">\
                        <a><h1>{}</h1></a>\
                        {}\
                        <p>{}</p>\
                    </div>\
                </li>".format(
                    img,
                    comment.user.username,
                    print_comment,
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )

        return HttpResponse(html)
