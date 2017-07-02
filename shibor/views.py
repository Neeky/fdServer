from django.shortcuts import render
from .models import ShiborRate
from django.http import HttpResponse
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
