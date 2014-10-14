# -*- coding: utf-8 -*-
from category.models import Category
from django.http import Http404

class RouteNav(object):
	"""docstring for RouteNav"""
	def __init__(self, category_id):
		super(RouteNav, self).__init__()
		self.__category_id = category_id
		self.route = []
		self.__get_category()

	def __get_category(self):
		try:
			cate = Category.objects.get(id = self.__category_id)
		except Category.DoesNotExist:
			raise Http404

		self.route.append(cate)
		self.__get_parent_cate(cate)

	def __get_parent_cate(self, base_cate):
		if base_cate.parent_category:
			self.route.append(base_cate.parent_category)
			self.__get_parent_cate(base_cate.parent_category)
		else:
			pass