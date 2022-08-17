from django.urls import path
from .views import (
    DemoInfoListView,
    PatientDetailView,
    DemoInfoCreateView,
    DemoInfoUpdateView,
    PatientDeleteView,
    PtntHistCreateView,
)
urlpatterns = [
    path('register/', DemoInfoCreateView.as_view(), name='register'),
    path('ptntList/', DemoInfoListView.as_view(), name='patientsListView'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patientDetail'),
    path('<int:pk>/ptnDemoUpdate/', DemoInfoUpdateView.as_view(), name='patientUpdate'),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name='patientDelete'),
    path('<int:pk>/casereport/', PtntHistCreateView.as_view(), name='historyCreate'),
]
