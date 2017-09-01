from django.shortcuts import render
from django.http      import HttpResponse,JsonResponse
from datetime         import datetime
from .models          import IndexOverview 
import json
# Create your views here.

def add_index_overview(self,request):
    try:
        datas=request.POST
        pushDate=datas['pushDate']
        currentRow=IndexOverview.objects.filter(pushDate__istartswith=pushDate)
        if len(currentRow)==0:
            io = IndexOverview()
            io.spe=datas['spe']
            io.dpe=datas['dpe']
            io.pb =datas['pb']
            io.dp =datas['dp']
            io.save()
            return HttpResponse('ok data has been saved')
        return HttpResponse('warn data has been in database')
    except Exception as e:
        em='exception in sse.view.addOverview --{0}'.format(e)
        print(em)
        return HttpResponse(em)
            
 
        


