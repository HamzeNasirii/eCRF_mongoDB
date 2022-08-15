from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import DemoInfo, HealthInfo
from .forms import MyModelForm


class DemoInfoCreateView(generic.CreateView):
    model = DemoInfo
    fields = ['d_first_name', 'd_last_name', 'd_national_code', 'd_gender', 'd_birthday', 'd_educate_rate',
              'd_economic_situation', 'd_status_job', 'a_province', 'a_town', 'a_village', 'a_post_code',
              'p_home_phone', 'p_cell_phone', 'p_fax', 'p_work_phone', 'p_cellular_phone', 'p_health_care_proxy_phone',
              'p_emergency_phone']
    form_class = MyModelForm
    template_name = 'eCRF/patient_register.html'
    # context_object_name = 'item'
    # success_url = reverse_lazy('home.html')


class DemoInfoListView(generic.ListView):
    model = DemoInfo
    template_name = 'eCRF/patients_list.html'
    context_object_name = 'patient_list'


class PatientDetailView(generic.DetailView): # باید تبدیل شود به create تا ثبت فرم گزارش مورد انجام شود
    model = DemoInfo
    template_name = 'eCRF/patent_detail_view.html'


class DemoInfoUpdateView(generic.UpdateView):
    model = DemoInfo
    fields = ['d_first_name', 'd_last_name', 'd_national_code', 'd_gender', 'd_birthday', 'd_educate_rate',
              'd_economic_situation', 'd_status_job', 'a_province', 'a_town', 'a_village', 'a_post_code',
              'p_home_phone', 'p_cell_phone', 'p_fax', 'p_work_phone', 'p_cellular_phone', 'p_health_care_proxy_phone',
              'p_emergency_phone']
    template_name = 'eCRF/patient_update.html'
    success_url = 'patient_list'


class PatientDeleteView(generic.DeleteView):
    model = DemoInfo
    fields = ['d_first_name', 'd_last_name', 'd_national_code', 'd_gender', 'd_birthday', 'd_educate_rate',
              'd_economic_situation', 'd_status_job', 'a_province', 'a_town', 'a_village', 'a_post_code',
              'p_home_phone', 'p_cell_phone', 'p_fax', 'p_work_phone', 'p_cellular_phone', 'p_health_care_proxy_phone',
              'p_emergency_phone']
    template_name = 'eCRF/patient_delete.html'
    success_url = 'patient_list'

