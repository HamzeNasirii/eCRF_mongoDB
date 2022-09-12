from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.chart, name='chart_view_page'),
]
