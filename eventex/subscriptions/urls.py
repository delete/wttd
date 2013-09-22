# coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.subscriptions.views',
	url(r'^(\d+)/$', 'detail', name='detail'),
	url(r'^inscritos/$', 'entries', name='entries'),
	url(r'^$', 'subscribe', name='subscribe'),
)
