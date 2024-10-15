from django.contrib import admin
from import_export.admin import *
from .models import *
 
# Register your models here.
class quizAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['question',  'op1','op2','op3','op4','op5']


admin.site.register(quiz, quizAdmin)

class datasetAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['emotion',  'option']


admin.site.register(dataset, datasetAdmin)
admin.site.register(mood)