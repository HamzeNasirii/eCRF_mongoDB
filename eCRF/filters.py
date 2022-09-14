
from .models import DemoInfo
import django_filters


class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = DemoInfo
        fields = '__all__'
