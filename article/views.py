#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from article.models import Article

# Create your views here.
def show_article(request, article_id = 0 ):
	try:
		article = Article.objects.get( id = article_id )
	except Article.DoesNotExist:
		raise Http404

#		title = request.POST[ 'title' ]
#		author = request.POST[ 'author' ]
#		content = request.POST[ 'content' ]


	context = {
		'article': article,
	}

	return render_to_response('article.html',context)
