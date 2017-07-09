from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import GlodPrice
import json
from datetime import datetime,date
# Create your views here.

def webClientPostHandler(request):
    """
    用于处理黄金交易所的当期数据进行入库
    """
    try:
        #得到当前的日期
        data=json.loads(request.body.decode('utf8'))
        year=datetime.now().year
        month=datetime.now().month
        day=datetime.now().day
        #如果当前日期在数据库中没有数据与之对应，那么就把数据写入库
        lastRows=GlodPrice.objects.filter(pushDate__istartswith='{0}-{1}-{2}'.format(year,month,day))
        if len(lastRows) == 0 and data['closingPrice'] != -1:
            #如果还没有收盘，那么默认情况下客户端会发送一个 -1 的收盘价给到服务器、就种情况下就不应该入库
            gp=GlodPrice()
            gp.fromJson(data)
            gp.save()
            return HttpResponse("ok")
        return HttpResponse("today is weekend can not upload data to database (glod)")
    except Exception as e:
        print(e)
        return HttpResponse("exception has occur in glod.view.webClientPostHandler")

def webClientPostHistoryHandler(request):
    """
    用于处理黄金交易所的历史数据进行入库
    """
    try:
        data=json.loads(request.body.decode('utf8'))
        lastRows=GlodPrice.objects.filter(pushDate__istartswith=data['pushDate'])
        if len(lastRows) == 0:
            gp=GlodPrice()
            gp.fromJson(data)
            year,month,day=[int(i) for i in data['pushDate'].split('-')]
            gp.pushDate=date(year,month,day)
            gp.save() 
        return HttpResponse("ok")
    except Exception as e:
        print(e)
        return HttpResponse("exception has occur in glod.views.webClientPostHistoryHandler")


def ajaxClientGetHandler(request):
    """
    """
    try:
        year=datetime.now().year - 8
        qs=GlodPrice.objects.filter(pushDate__year__gte=year)
        pushDate=[str(v.pushDate)[:10] for v in qs ]
        datas=[ [float(v.openingPrice),float(v.closingPrice),float(v.minimumPrice),float(v.highestPrice)] for v in qs]

        #openingPrice=[float(v.openingPrice) for v in qs ]
        #closingPrice=[float(v.closingPrice) for v in qs ]
        #highestPrice=[float(v.highestPrice) for v in qs ]
        #minimumPrice=[float(v.minimumPrice) for v in qs ]
        return JsonResponse({
            'pushDate':pushDate,
            'datas':datas
            #'openingPrice':openingPrice,
            #'closingPrice':closingPrice,
            #'highestPrice':highestPrice,
            #'minimumPrice':minimumPrice,
            })
    except Exception as e:
        print(e)
        return HttpResponse('error ocurr in glod.views.ajaxClientGetHandler')









