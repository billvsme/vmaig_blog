from django.conf.urls import patterns,url
from vmaig_comments.views import CommentControl


urlpatterns = patterns("",
        url(r'^comment/(?P<slug>\w+)$',CommentControl.as_view()),
    )
