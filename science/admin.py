from django.contrib import admin
from science.models import Science

# Register your models here.
class ScienceAdmin(admin.ModelAdmin):
	list_display = ( 'project_title', 'project_person_in_charge', 'project_time',)


admin.site.register(Science,ScienceAdmin)	
