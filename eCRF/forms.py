from eCRF.models import DemoInfo
from django import forms


class MyModelForm(forms.ModelForm):
    class Meta:
        model = DemoInfo
        fields = ['d_educate_rate']
