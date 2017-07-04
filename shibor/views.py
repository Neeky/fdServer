from django.shortcuts import render
from .models import ShiborRate
from django.http import HttpResponse,JsonResponse
from datetime import datetime,date
import json

# Create your views here.
def webClientPostHandler(request):
    """
    处理由webclient提交的数据
    """
    try:
        #从body中解析出数据
        data=json.loads(request.body.decode('utf8'))
        lastRows=ShiborRate.objects.filter(pushDate__istartswith=data['pushDate'])
        if len(lastRows)== 0:
            #如果数据还没有入库那么就入库
            newRow=ShiborRate()
            newRow.fromJson(data)
            newRow.save()
        return HttpResponse("ok")
    except Exception as e:
        print(e)
        return HttpResponse('exception has append in function shibor.webClientPostHandler')

def initClientPostHandler(request):
    """
    处理init发出的请求，init发来的数据是shibor的历史数据
    """
    try:
        data=request.POST
        row=ShiborRate.objects.filter(pushDate__istartswith=data['pushDate'])
        if len(row) == 0:
            newRow=ShiborRate()
            newRow.fromJson(data)
            newRow.save()
        return HttpResponse("ok")
    except Exception as e:
        print(e)
        return HttpResponse('exception has append in function shibor.initClientPostHandler')

def ajaxClientGetHandler(request):
    """
    用于完成对shibor历史记录的查询
    """
    try:
        year=datetime.now().year - 3
        rows=ShiborRate.objects.filter(pushDate__year__gte=year)
        pushDate=[str(v.pushDate)[:10] for v in rows]
        oneNight=[float(v.oneNight) for v in rows]
        oneWeek=[float(v.oneWeek) for v in rows]
        twoWeek=[float(v.twoWeek) for v in rows]
        oneMonth=[float(v.oneMonth) for v in rows]
        threeMonth=[float(v.threeMonth) for v in rows]
        sixMonth=[float(v.sixMonth) for v in rows]
        nineMonth=[float(v.nineMonth) for v in rows]
        oneYear=[float(v.oneYear) for v in rows]
        return JsonResponse({'pushDate':pushDate,
            'oneNight':oneNight,
            'oneWeek':oneWeek,
            'twoWeek':twoWeek,
            'oneMonth':oneMonth,
            'threeMonth':threeMonth,
            'sixMonth':sixMonth,
            'nineMonth':nineMonth,
            'oneYear':oneYear
            })
    except Exception as e:
        print(e)
        return JsonResponse({'k':'error in shibor.views.ajaxClientGetHandler'})

    















    
