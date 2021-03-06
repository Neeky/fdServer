from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import MoneySupply
from datetime import datetime,date
import json

# Create your views here.
def webClientPostHandler(request):
    try:
        data=json.loads(request.body.decode('utf8'))
        rows=MoneySupply.objects.filter(pushDate__istartswith=data['pushDate'])
        if(len(rows)==0):
            ms=MoneySupply()
            ms.fromJson(data)
            ms.save()
        return HttpResponse("ok")
    except Exception as e:
        print(e)
        return HttpResponse('exception has append in function pbc.views.webClientPostHandler')
    

def ajaxClientGetHandler(request):
    """
    """
    try:
        year=datetime.now().year - 10
        rows=MoneySupply.objects.filter(pushDate__year__gte=year)
        pushDate=[str(v.pushDate)[:10] for v in rows]
        m0=[float(v.m0) for v in rows]
        m1=[float(v.m1) for v in rows]
        m2=[float(v.m2) for v in rows]
        return JsonResponse({'pushDate':pushDate,'m0':m0,'m1':m1,'m2':m2})
    except Exception as e:
        print(e)
        return JsonResponse({'k':'error in pbc.views.ajaxClientGetHandler'})

def getLastMoneySupply(request):
    """
    """
    try:
        year=datetime.now().year -1
        row=MoneySupply.objects.all()
        print(len(row))
        row=row[len(row)-1]
        return JsonResponse({'m0':float(row.m0)*10000000,'m1':float(row.m1)*10000000,'m2':float(row.m2)*10000000})
    except Exception as e:
        em='error eccur in pbc.views.getLastMoneySupply -- message {0}'.format(e)
        print(em)
        return HttpResponse(em)



