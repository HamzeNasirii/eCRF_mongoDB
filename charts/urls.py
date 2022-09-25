from django.urls import path
from .views import gender_report_table, gender_report_chart

urlpatterns = [
    path('chart/', gender_report_chart, name='gender_chart_report'),
    path('report/', gender_report_table, name='gender_report_tbl'),
]
