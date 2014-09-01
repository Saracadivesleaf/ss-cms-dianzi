#coding=utf-8
from django.db import models
from category.models import Category

# Create your models here.
class Article(models.Model):
	""" docting for Articles """

	class Meta:
		verbose_name = u'文章'
		verbose_name_plural = verbose_name

	title = models.CharField(max_length = 100, verbose_name = u'标题')
	author = models.CharField(max_length = 30, verbose_name = u'作者')
	publish_time = models.DateTimeField(auto_now_add = True, verbose_name = u'发表时间')
	update_time = models.DateTimeField(auto_now = True, verbose_name = u'更新时间')
	content = models.TextField(verbose_name = u'文章内容')
	classify = models.ForeignKey(Category, verbose_name = u'分类')
	page_view = models.IntegerField(null = True, verbose_name = u'访问量')

	def __unicode__(self):
		return self.title
