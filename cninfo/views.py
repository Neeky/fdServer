from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Company
import json
from datetime import datetime,date,timedelta

# Create your views here.

def addCompany(request):
    """
    处理客户端收集到的公司信息
    """
    try:
        data=json.loads(request.body.decode('utf8'))
        rows=Company.objects.filter(stockCode=data['stockCode'])
        if (len(rows) == 0):
            ci=Company()
            ci.fromJson(data)
            ci.save()
            return HttpResponse("ok")
        pass
    except Exception as e:
        em='exception occur in cninfo.views.addCompany message -- {0}'.format(e)
        print(em)
        return HttpResponse(em)

def listCompanys(request):
    """
    """
    companys=None
    try:
        companys=Company.objects.all()
        rs=[[v.stockCode,v.mainPage] for v in companys]
        return JsonResponse({'companys':rs})
    except Exception as e:
        em='exception occur in cninfo.views.listCompany message -- {0}'.format(e)
        print(em)
        return HttpResponse(em)

        
def updateCompanyBriefInfo(request):
    """
    """
    row=None
    try:
        data=json.loads(request.body.decode('utf8'))
        rows=Company.objects.filter(stockCode=data['stockCode'])
        if len(rows) != 0:
            row=rows[0]
            row.fromJsonAddBrief(data)
            row.lastUpdate=datetime.now()
            row.save()
            return HttpResponse("ok")
    except Exception as e:
        if row != None:
            row.lastUpdate=datetime.now()
            row.save()
        em='exception occur in cninfo.views.updateComanyBriefInfo message -- {0}'.format(e) 
        print(em)
        return HttpResponse(em)

def getTask(request):
    """
    """
    try:
        now=datetime.now()
        today=datetime(year=now.year,month=now.month,day=now.day,hour=0,minute=0,second=0)
        rows=Company.objects.filter(lastUpdate__lt=today)
        if len(rows) >=1:
            rs=[rows[0].stockCode,rows[0].mainPage]
            return JsonResponse({'company':rs})
        else:
            return JsonResponse({'company':[0,0]});
    except Exception as e:
        em='exception occur in cninfo.views.getTask message --{0}'.format(e)
        print(em)
        return HttpResponse(em)




 
