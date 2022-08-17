from django.contrib import admin
from .models import DemoInfo, PatientHistory


@admin.register(DemoInfo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['d_national_code', 'd_first_name', 'd_last_name', ]


@admin.register(PatientHistory)
class PtntHistoryAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'chronic_disease', 'PCR_test_resul', 'allergy', ]
# Register your models here.
