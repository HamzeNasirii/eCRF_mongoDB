from django.contrib import admin
from .models import DemoInfo


@admin.register(DemoInfo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['d_national_code', 'd_first_name', 'd_last_name', ]

# Register your models here.
