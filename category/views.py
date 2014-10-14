from django.shortcuts import render_to_response
from django.http import Http404
from category.models import Category
from category.routenav import RouteNav
from article.models import Article

# Create your views here.
def get_article_list_by_category(request, category_id):
	if category_id == 0:
		article_list = Article.objects.all()
	else:
		try:
			catagory_get = Category.objects.get(id=category_id)
		except Category.DoesNotExist:
			raise Http404
		article_list = Article.objects.filter(classify=catagory_get)

	nav = RouteNav(category_id)
	routelist = nav.route[::-1]

	output = {
		'page_title': catagory_get.category_name,
		'nav': routelist,
		'article_list': article_list,
	}


	return render_to_response('list.html', output)
