from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from market.models import InvestorSituation , ShiborRate,StockIndex
from django.db.models import Q

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

def add_or_update_stock_index(request):
    """
    增加股指信息
    """
    post=request.POST
    target_row=None
    em=""
    try:
        #获取目标行
        target_row=StockIndex.objects.get(Q(push_date=post['push_date']),Q(index_name=post['index_name']))
    except StockIndex.DoesNotExist as e:
        #如果目标行不存在，就创建一个新行
        target_row=StockIndex()
    except Exception as e:
        #为其它可能就异常留下空位
        em="warn exception in market.views.add_stock_index :{0}".format(e)
    #如果目标行不是空，那么就可以对它进入操作了
    if target_row != None:
        #把push_date和index_name设置一下，这个动作对于insert是必要的，对于update是无害的
        target_row.push_date=post['push_date']
        target_row.index_name=post['index_name']
        #由于这个函数要处理两个不同的更新逻辑，不同的逻辑传来的参数又不一样，所以这里用open_value来区分
        if 'open_value' in post and target_row.open_value == 0:
            target_row.open_value=post['open_value']
            target_row.close_value=post['close_value']
            target_row.higest_value=post['higest_value']
            target_row.lowest_value=post['lowest_value']
            target_row.fluctuation=post['fluctuation']
            target_row.transaction_amount=post['transaction_amount']
            if 'total_market_value' in post and target_row.total_market_value ==0:
                target_row.total_market_value=post['total_market_value']
                target_row.transaction_amount=post['transaction_amount']
                target_row.circulation_market_value=post['circulation_market_value']
        elif target_row.spe == 0 and 'spe' in post:
            target_row.spe  =post['spe']
            target_row.dpe  =post['dpe']
            target_row.pb   =post['pb']
            target_row.dp   =post['dp']
            target_row.lyspe=post['lyspe']
            target_row.lydpe=post['lydpe']
            target_row.lypb =post['lypb']
        target_row.save()
        em="ok data been inserted or updated"
    return HttpResponse(em)


        
    


