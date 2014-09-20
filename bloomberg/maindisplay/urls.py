from django.conf.urls import patterns, url

from maindisplay import views


urlpatterns = patterns ('',
	url(r'^$',views.start, name='startPage'),
	url(r'^(?P<company_tag>\w+)/$', views.home, name='home'),
	url(r'^(?P<company_tag>\w+)/get/last_call=(?P<last_call>\d+)/$', views.getJSON, name="getJSON"),
)