from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from market.models import InvestorSituation , ShiborRate

# Create your views here.

def add_investor_situation(request):
    """
    增加投资者信息到数据库
    1、确定要增加的数据有没有在数据库中
    2、如果没有就把数据入库
    """
    post=request.POST
    try:
        targe_row=InvestorSituation.objects.get(push_date=post['push_date'])
    except InvestorSituation.DoesNotExist  as e:
        """
        如果target_row在数据库中没有命中，说明就要把它加入数据库
        """
        investor=InvestorSituation.fromPostInit(request.POST)
        investor.save()
        em="ok data been inserted "
        return HttpResponse(em)
    except Exception as e:
        em="warn exception in market.add_investor_situation : {0}".format(e)
        return HttpResponse(em)
    message="warn data maybe already in database"
    return HttpResponse(message)


def add_shibor_rate(request):
    """
    增加shibor相关数据到数据库
    1、确认要入库的数据，目前在不在数据库中。
    2、如果没有就把它入库。
    """
    post=request.POST
    try:
        target_row=ShiborRate.objects.get(push_date=post['push_date'])
    except ShiborRate.DoesNotExist as e:
        shibor=ShiborRate.fromPostInit(post)
        shibor.save()
        em="ok data been inserted"
        return HttpResponse(em)
    except Exception as e:
        em="warn execption in market.add_shibor_rate :{0}".format(e)
        return HttpResponse(em)
    message="warn data maybe already in database"
    return HttpResponse(message)


    


