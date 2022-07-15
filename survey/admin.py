from django.contrib import admin
from .models import Survey

# Register your models here.


class SurveyAdmin(admin.ModelAdmin):
    list_display = ['pk','user','age','survey']
    #list_filter = ['title']
    #prepopulated_fields = {'slug':['name']}

admin.site.register(Survey, SurveyAdmin)

#admin.site.register(Survey)