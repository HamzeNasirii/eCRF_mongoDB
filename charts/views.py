from django.http import HttpResponse
from django.shortcuts import render
from allauth.account.forms import LoginForm
from eCRF.models import *
import pandas as pd


# ---------------------------------------- LOGIN Check------------------
# class MyCustomLoginForm(LoginForm):
#     def login(self, *args, **kwargs):
#         # Add your own processing here.
#
#         # You must return the original result.
#         return super(MyCustomLoginForm, self).login(*args, **kwargs)


# ---------------------------------------------------------------SHOW TBL------------

def gender_report_table(request):
    # item = DemoInfo.objects.all()
    # if request.user.is_authenticated:
    context = {
        # gender report tbl
        'gender_items': DemoInfo.get_gender_count_info(),
        # educate report tbl
        'educate_items': DemoInfo.get_educate_count_info(),
        # economic report tbl
        'economic_items': DemoInfo.get_economic_count_info(),
        # status job report tbl
        'status_job_items': DemoInfo.get_job_status_count_info()
    }
    return render(request, 'charts/chart_view.html', context)


# else:
#     return render(request, 'account/login.html')


# ---------------------------------------------------------------SHOW CHARTS------------
def gender_report_chart(request):
    context = {
        'man_count': int(DemoInfo.objects.filter(d_gender='man').count()),
        'women_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        'ukw_count': int(DemoInfo.objects.filter(d_gender='ukw').count()),
        'illit_count': int(DemoInfo.objects.filter(d_educate_rate='illit').count()),
        'elmnt_count': int(DemoInfo.objects.filter(d_educate_rate='elmnt').count()),
        'dplom_count': int(DemoInfo.objects.filter(d_educate_rate='dplom').count()),
        'tchnc_count': int(DemoInfo.objects.filter(d_educate_rate='tchnc').count()),
        'exprt_count': int(DemoInfo.objects.filter(d_educate_rate='exprt').count()),
        'Mstrs_count': int(DemoInfo.objects.filter(d_educate_rate='Mstrs').count()),
        'Phd_count': int(DemoInfo.objects.filter(d_educate_rate='Phd').count()),
        'low_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        'norm_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        'good_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        'best_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '1_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '2_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '3_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '4_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '5_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '6_count': int(DemoInfo.objects.filter(d_gender='wom').count()),
        '7_count': int(DemoInfo.objects.filter(d_gender='wom').count())
    }
    return render(request, 'charts/chart_report.html', context)
