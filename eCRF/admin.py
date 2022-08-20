from django.contrib import admin
from .models import DemoInfo, PatientHistory


@admin.register(DemoInfo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['d_national_code', 'd_first_name', 'd_last_name', 'd_birthday', 'd_gender', 'datetime_created',
                    'datetime_modified']


@admin.register(PatientHistory)
class PtntHistoryAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'chronic_disease', 'PCR_test_resul', 'allergy', 'datetime_modified',
                    'datetime_created']
# Register your models here.
