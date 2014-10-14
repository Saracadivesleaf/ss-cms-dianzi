#coding=utf-8
from django.db import models

# Create your models here.
class Category(models.Model):
	""" docting for Categorys """

	class Meta:
		verbose_name = u'类别'
		verbose_name_plural = verbose_name

	id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=30, verbose_name=u'类别名')
	parent_category = models.ForeignKey('Category', null=True, blank=True, verbose_name=u'父类别')

	def __unicode__(self):
		return self.category_name

	def get_absolute_url(self):
		return '/list/%d' % self.id