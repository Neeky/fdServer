from django.shortcuts import render
from django.http      import HttpResponse,JsonResponse
from .models          import MarketOverview
from datetime         import datetime
import json

# Create your views here.

def addOverview(request):
    """
    chanceClient post sseOverview时用到
    """
    try:
        datas=request.POST
        pushDate=datas['pushDate']
        currentRow=MarketOverview.objects.filter(pushDate__istartswith=pushDate)
        if(len(currentRow)==0):
            mo                 =MarketOverview()
            mo.pushDate        =datas['pushDate']
            mo.totalValue      =datas['totalValue']
            mo.circulationValue=datas['circulationValue']
            mo.tradValue       =datas['tradValue']
            mo.turnoverRate    =datas['turnoverRate']
            mo.PERate          =datas['PERate']
            mo.pushDate        =datas['pushDate']
            mo.save()
            return HttpResponse('ok data been saved')
        else:
            return HttpResponse('warn data has been in database')
    except Exception as e:
        em='exception in sse.view.addOverview --{0}'.format(e)
        print(em)
        return HttpResponse(em)    
