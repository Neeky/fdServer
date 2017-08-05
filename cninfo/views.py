from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from .models import Company
import json
from datetime import datetime,date,timedelta
from collections import Counter

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
        rows=Company.objects.filter(Q(lastUpdate__lt=today),Q(section='深市主板') | Q(section='中小企业板') | 
        Q(section='创业板') | Q(section='沪市主板'))
        if len(rows) >=1:
            rs=[rows[0].stockCode,rows[0].mainPage]
            return JsonResponse({'company':rs})
        else:
            return JsonResponse({'company':[0,0]});
    except Exception as e:
        em='exception occur in cninfo.views.getTask message --{0}'.format(e)
        print(em)
        return HttpResponse(em)

def listCompanyCountByIndustry(request):
    """
    """
    try:
        rows=Company.objects.filter(Q(section='深市主板') | Q(section='中小企业板') |
        Q(section='创业板') | Q(section='沪市主板'))
        rowsCache=[row for row in rows]
        industrys=[row.industry for row in rowsCache]
        industryCounter=Counter()
        for industry in industrys:
           industryCounter[industry]+=1
        res=[[key,industryCounter[key]] for key in industryCounter.keys()]
        inds=[key for key in industryCounter.keys()]
        print(inds)
        count=[industryCounter[key] for key in inds ]
        inds=[i if i !='' else '其它' for i in inds ]
        return JsonResponse({'industrys':inds,'counters':count},json_dumps_params={'ensure_ascii':False})
    except Exception as e:
        em="exception in cninfo.views.getCompanyCountByIndustry : {0}".format(e)
        print(em)
        return HttpResponse(em)

 
