from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from eCRF.models import *


# ---------------------------------------------------------------SHOW TBL------------
def gender_report_table(request):
    # item = DemoInfo.objects.all()
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


# ---------------------------------------------------------------SHOW CHARTS------------
def gender_report_chart(request):
    item = DemoInfo.objects.all().values()
    df = pd.DataFrame(item)
    df1 = df.d_gender.tolist()
    gender_items: DemoInfo.get_gender_count_info()
    df = df['gender_items'].tolist()
    mydict = {
        'df': df,
        'df1': df1,
    }
    return render(request, 'charts/chart_report.html', context=mydict)
# def gender_report_chart(request):
#     # [[6, 10]], columns = ['a', 'b']
#     # item = DemoInfo.objects.all().values()
#     # df = pd.DataFrame(item)
#     # df.name = 't'
#     # df1 = df.name
#     # df = df['d_gender'].tolist()
#     # mydict = {
#     #     'df': df,
#     #     'df1': df1,
#     # }
#     context = {
#         'gender_items': DemoInfo.get_gender_count_info()
#     }
# return render(request, 'charts/chart_report.html')

# def testing(request):
#     mydata = DemoInfo.objects.filter(d_gender='مرد').count()
#     template = 'charts/chart_view.html'
#     context = {
#         'mymembers': mydata,
#     }
#     return HttpResponse(template.render(context, request))
