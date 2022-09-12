from django.http import HttpResponse
from django.shortcuts import render
from eCRF.models import *
import pandas as pd


def chart(request):
    # item = DemoInfo.objects.all().values()
    man = int(DemoInfo.objects.filter(d_gender='man').count())
    woman = int(DemoInfo.objects.filter(d_gender='wom').count())
    context = {
        'man_count': man,
        'woman_count': woman,
    }
    print(man, woman)

    # [[6, 10]], columns = ['a', 'b']
    # df = pd.DataFrame(man)
    # df.name = 't'
    # df1 = df.name
    # df = df['d_gender'].tolist()
    # mydict = {
    #     'df': df,
    #     'df1': df1,
    # }
    return render(request, 'charts/chart_view.html', context)


# def testing(request):
#     mydata = DemoInfo.objects.filter(d_gender='مرد').count()
#     template = 'charts/chart_view.html'
#     context = {
#         'mymembers': mydata,
#     }
#     return HttpResponse(template.render(context, request))
