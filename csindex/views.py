from django.shortcuts import render
from django.http      import HttpResponse,JsonResponse
from datetime         import datetime
from .models          import IndexOverview,IndexDetail
from django.db.models import Q
import json
# Create your views here.

def add_index_overview(request):
    try:
        datas=request.POST
        pushDate=datas['pushDate']
        indexName=datas['indexName']
        currentRow=IndexOverview.objects.filter(Q(pushDate__istartswith=pushDate),Q(indexName=indexName))
        if len(currentRow)==0:
            io = IndexOverview()
            io.spe=datas['spe']
            io.dpe=datas['dpe']
            io.pb =datas['pb']
            io.dp =datas['dp']
            io.pushDate=pushDate
            io.indexName=datas['indexName']
            io.save()
            return HttpResponse('ok data has been saved')
        return HttpResponse('warn data has been in database')
    except Exception as e:
        em='exception in sse.view.add_index_overview --{0}'.format(e)
        print(em)
        return HttpResponse(em)
            
 
def add_index_detail(request):
    try:
        datas=request.POST
        pushDate=datas['pushDate']
        indexName=datas['indexName']
        currentRow=IndexDetail.objects.filter(Q(pushDate__istartswith=pushDate),Q(indexName=indexName))
        if len(currentRow) ==0:
            ind=IndexDetail()
            ind.pushDate=pushDate
            ind.indexName=indexName
            ind.delta=datas['delta']
            ind.deltaPercent=datas['deltaPercent']
            ind.save()
            return HttpResponse('ok data has been saved')
        return HttpResponse('warn data has been in database')
    except Exception as e:
        em='exception in sse.view.add_index_detail --{0}'.format(e)
        print(em)
        return HttpResponse(em) 


