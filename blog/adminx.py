#coding:utf-8
from blog.models import Article,Category,Carousel,Nav,Column,News

import xadmin
from xadmin.layout import Main, Fieldset

class CategoryAdmin(object):
    search_fields = ('name',)
    list_filter = ('status','create_time')
    list_display = ('name','parent','rank','status')
    fields = ('name','parent','rank','status')



class ArticleAdmin(object):
    search_fields = ('title','summary')
    list_filter = ('status','category','is_top','create_time','update_time','is_top')
    list_display = ('title','category','author','status','is_top','update_time')

    form_layout = (
        Fieldset(u'基本信息',
                    'title','en_title','img','category','tags','author','is_top','rank','status'
                    ),
        Fieldset(u'内容',
                    'content'
                    ),
        Fieldset(u'摘要',
                    'summary'
                    ),
        Fieldset(u'时间',
                    'pub_time'
                    )
    )


class NewsAdmin(object):
    search_fields = ('title','summary')
    list_filter = ('news_from','create_time')
    list_display = ('title','news_from','url','create_time')
    fields = ('title','news_from','url','summary','pub_time')


class NavAdmin(object):
    search_fields = ('name',)
    list_display = ('name','url','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','url','status')


class ColumnAdmin(object):
    search_fields = ('name',)
    list_display = ('name','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','status','article','summary')
    filter_horizontal = ('article',)


class CarouselAdmin(object):
    search_fields = ('title',)
    list_display = ('title','article','img','create_time')
    list_filter = ('create_time',)
    fields = ('title','article','img','summary')


class GlobalSetting(object):
    site_title = u"Vmaig后台管理"
    site_footer = u"vmaig.com"


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "欢迎",
            "content": "<h3> Welcome to Vmaig! </h3>\
                        <p>欢迎来到 Vmaig ,如果有任何问题可以加:<br/>\
                        我的QQ：994171686<br/>\
                        QQ群：458788510 <br/><br/>\
                        后台中，可以<br/>\
                        通过“轮播”添加首页的轮播<br/>\
                        通过“导航条”添加首页nav中的项目<br/>\
                        通过“专栏” 添加博客专栏（可以和导航条结合起来）<br/>\
                        通过“资讯” 添加转载的新闻<br/>\
                        通过“分类” “文章” 添加分类跟文章<br/>\
                        通过“用户” 对用户进行操作<br/>\
                        <h3>注意</h3>\
                        左边的Revisions没用，不用管它<br/>\
                        首页的便签云中的内容，在后台不能修改。 请修改 blog/templates/blog/widgets/tags_cloud.html 中的 tags数组的内容。<br/><br/>"},
        ],
    ]


xadmin.site.register(xadmin.views.CommAdminView,GlobalSetting)
xadmin.site.register(xadmin.views.website.IndexView, MainDashboard)

xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(News,NewsAdmin)
xadmin.site.register(Nav,NavAdmin)
xadmin.site.register(Column,ColumnAdmin)
xadmin.site.register(Carousel,CarouselAdmin)
