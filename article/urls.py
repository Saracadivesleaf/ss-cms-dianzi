from django.conf.urls import patterns, url

urlpatterns = patterns('article.views',
	url(r'^\d+/', 'show_article'),
	)