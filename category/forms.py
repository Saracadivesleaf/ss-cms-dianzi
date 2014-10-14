# -*- coding: utf-8 -*-
from django.forms import ModelForm
from category.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'parent_category']
