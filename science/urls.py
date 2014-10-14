# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('science.views',
	url(r'^$', 'science'),
	)