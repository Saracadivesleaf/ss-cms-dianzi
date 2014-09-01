from django.shortcuts import render_to_response
from django.http import Http404
from catagory.models import Category
from article.models import Article

# Create your views here.
def get_article_list_by_category(request, category_id=0):
	if category_id == 0:
		article_list = Article.objects.all()
	else:
		try:
			catagory_get = Category.objects.get(id=category_id)
		except Category.DoesNotExist:
			raise Http404
		article_list = Article.objects.filter(classify=catagory_get)
