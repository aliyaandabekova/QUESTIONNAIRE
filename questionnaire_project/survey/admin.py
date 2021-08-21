from django.contrib import admin
from .models import *

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    readonly_fields = ['start_date']
admin.site.register(Survey,SurveyAdmin)

admin.site.register([Question,Answer])
