from django.conf.urls import url
from blog.views import (IndexView, ArticleView, AllView, SearchView,
                        ColumnView, UserView, NewsView, TagView, CategoryView)
from django.views.generic import TemplateView, DetailView
from blog.models import News

urlpatterns = [
        url(r'^$', IndexView.as_view(), name='index-view'),
        url(r'^article/(?P<slug>\w+).html$',
            ArticleView.as_view(), name='article-detail-view'),
        url(r'^all/$', AllView.as_view(), name='all-view'),
        url(r'^search/$', SearchView.as_view()),
        url(r'^login/$',
            TemplateView.as_view(template_name="blog/login.html")),
        url(r'^register/$',
            TemplateView.as_view(template_name="blog/register.html")),
        url(r'^forgetpassword/$',
            TemplateView.as_view(template_name="blog/forgetpassword.html")),
        url(r'^resetpassword/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            TemplateView.as_view(template_name="blog/resetpassword.html")),
        url(r'^column/(?P<column>\w+)/$',
            ColumnView.as_view(), name='column-view'),
        url(r'^user/(?P<slug>\w+)$', UserView.as_view()),
        url(r'^news/$', NewsView.as_view(), name='new-view'),
        url(r'^news/(?P<pk>\w+)$',
            DetailView.as_view(model=News), name='news-detail-view'),
        url(r'^tag/(?P<tag>\w+)/$', TagView.as_view(), name='tag-view'),
        url(r'^category/(?P<category>\w+)/$',
            CategoryView.as_view(), name='category-view'),
]
