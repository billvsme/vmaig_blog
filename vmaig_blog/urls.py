from django.conf.urls import include, url

#from django.contrib import admin
import xadmin

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls),name='xadmin'),
    url(r'',include('blog.urls')),
    url(r'',include('vmaig_comments.urls')),
    url(r'',include('vmaig_auth.urls')),
]
