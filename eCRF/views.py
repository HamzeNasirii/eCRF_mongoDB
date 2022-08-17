from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import DemoInfo, PatientHistory


# from .forms import MyModelForm

class PtntHistCreateView(generic.CreateView):
    model = PatientHistory
    fields = ['chronic_disease', 'PCR_test_resul', 'allergy']
    template_name = 'eCRF/case_report_form.html'
    context_object_name = 'patient_hist'

    def get_success_url(self):
        return reverse_lazy('patientsListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ptnthistory_info_models'] = PatientHistory.objects.all()
        context['model_chronic_disease_choices'] = PatientHistory.STATUS_CHRONIC
        context['model_pcr_choices'] = PatientHistory.STATUS_PCR
        context['model_allergy_choices'] = PatientHistory.STATUS_ALLERGY
        return context


class DemoInfoCreateView(generic.CreateView):
    model = DemoInfo
    fields = ['d_first_name', 'd_last_name', 'd_national_code', 'd_gender', 'd_birthday', 'd_educate_rate',
              'd_economic_situation', 'd_status_job', 'a_country', 'a_province', 'a_town', 'a_village', 'a_post_code',
              'p_home_phone', 'p_cell_phone', 'p_fax', 'p_work_phone', 'p_cellular_phone', 'p_health_care_proxy_phone',
              'p_emergency_phone']
    template_name = 'eCRF/patient_register.html'

    def get_success_url(self):
        return reverse_lazy('patientsListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo_info_models'] = DemoInfo.objects.all()
        context['model_gender_choices'] = DemoInfo.GENDER
        context['model_ecu_choices'] = DemoInfo.EDUCATE_RATE
        context['model_eco_choices'] = DemoInfo.ECONOMIC_SITUATION
        context['model_job_choices'] = DemoInfo.STATUS_JOB
        return context


class DemoInfoListView(generic.ListView):
    model = DemoInfo
    template_name = 'eCRF/patients_list.html'
    context_object_name = 'patient_list'


class PatientDetailView(generic.DetailView):  # باید تبدیل شود به create تا ثبت فرم گزارش مورد انجام شود
    model = DemoInfo
    template_name = 'eCRF/patent_detail_view.html'
    context_object_name = 'patient_detail'


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
