from django.conf.urls import patterns,url
from vmaig_auth.views import UserControl


urlpatterns = patterns("",
        url(r'^usercontrol/(?P<slug>\w+)$',UserControl.as_view()),
        )
