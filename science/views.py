from django.shortcuts import render_to_response
from django.http import Http404
from science.models import Science
from category.routenav import RouteNav
from category.models import Category

# Create your views here.
def get_progect_by_category(request, category_id):

	if category_id == 0:
		sciences_list = Science.objects.all()
	else:
		try:
			category_get = Category.objects.get(id = category_id)
		except Category.DoesNotExist:
			raise Http404
		sciences_list = Science.objects.filter(classify = category_get)

	nav = RouteNav(category_id)
	routelist = nav.route[::-1]

	output = {
		'project_title': catagory_get.category_name,
		'nav': routelist,
		'science_list': science_list,
	}

	return render_to_response('sciences.html')