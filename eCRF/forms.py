from django import forms
from .models import PatientHistory


class NewCaseReportForm(forms.ModelForm):
    class Meta:
        model = PatientHistory
        fields = [
            'national_code', 'chronic_disease', 'PCR_test_resul', 'allergy'
        ]

