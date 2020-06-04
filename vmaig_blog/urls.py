from django.urls import include, re_path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.urls import reverse

from django.contrib import admin

from blog.models import Article, News, Category, Column


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['index-view', 'news-view']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'article-is-top': GenericSitemap(
                {
                    'queryset': Article.objects.filter(
                                    status=0, is_top=True
                                ).all(),
                    'date_field': 'pub_time'
                },
                priority=1.0,
                changefreq='daily'
            ),
    'article-is-not-top': GenericSitemap(
                {
                    'queryset': Article.objects.filter(status=0).all(),
                    'date_field': 'pub_time'
                },
                priority=0.8,
                changefreq='daily'
            ),
    'news': GenericSitemap(
                {
                    'queryset': News.objects.all(),
                    'data_field': 'pub_time'
                },
                priority=0.6,
                changefreq='daily'
            ),
    'category': GenericSitemap(
                {
                    'queryset': Category.objects.all()
                },
                priority=0.9,
                changefreq='daily'
            ),
    'column': GenericSitemap(
                {
                    'queryset': Column.objects.all()
                },
                priority=0.9,
                changefreq='daily'
            ),
    'static': StaticViewSitemap
}


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),
    re_path(r'', include('vmaig_comments.urls')),
    re_path(r'', include('vmaig_auth.urls')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
