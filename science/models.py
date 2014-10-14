# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Science(models.Model):
	"""docstring for Science"""
	class Meta:
		verbose_name= u'科学研究'
		verbose_name_plural = verbose_name

	project_title = models.CharField(max_length=100, verbose_name='项目名称')
	project_person_in_charge = models.CharField(max_length=50, verbose_name='项目负责人')
	project_time = models.DateTimeField(auto_now_add=False, verbose_name='项目时间')

	
	def __unicode__(self):
		return self.project_title

	def get_absolute_url(self):
		return '/science/%d' % self.id
