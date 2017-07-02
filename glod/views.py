from django.shortcuts import render
from django.http import HttpResponse
from .models import GlodPrice
import json
from datetime import datetime,date
# Create your views here.

def webClientPostHandler(request):
    try:
        data=json.loads(request.body.decode('utf8'))
        year=datetime.now().year
        month=datetime.now().month
        day=datetime.now().day
        lastRows=GlodPrice.objects.filter(pushDate__istartswith='{0}-{1}-{2}'.format(year,month,day))
        if len(lastRows) == 0 and data['closingPrice'] != -1:
            gp=GlodPrice()
            gp.fromJson(data)
            gp.save()
            return HttpResponse("ok")
        return HttpResponse("today is weekend can not upload data to database (glod)")
    except Exception as e:
        print(e)
        return HttpResponse("exception has occur in glod.view.webClientPostHandler")
