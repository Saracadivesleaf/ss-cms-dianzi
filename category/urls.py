from django.conf.urls import patterns, url

urlpatterns = patterns('category.views',
	url(r'^\d+/$', 'get_article_list_by_category'),
	)