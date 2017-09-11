from django.db import models
from django.http import request

# Create your models here.
class InvestorSituation(models.Model):
    """
    投资者情况追踪
    """
    push_date               =models.DateField(help_text="发布时间",primary_key=True)
    new_investor            =models.DecimalField(help_text="新增投资者数量",max_digits=16,decimal_places=4)
    new_natural_person      =models.DecimalField(help_text="新增自然人投资者数量",max_digits=16,decimal_places=4)
    new_non_natural_person  =models.DecimalField(help_text="新增非自然人投资者数量",max_digits=16,decimal_places=4)
    final_investor          =models.DecimalField(help_text="期末投资者数量",max_digits=16,decimal_places=4)
    final_natural_person    =models.DecimalField(help_text="期末自然人投资者数量",max_digits=16,decimal_places=4)
    final_non_natural_person=models.DecimalField(help_text="期末非自然人投资者数量",max_digits=16,decimal_places=4)

    @classmethod
    def fromPostInit(cls,post):
        """
        从POST发来的数据初始化一个InverstorSituation 实例
        """
        investor                         =InvestorSituation()
        investor.push_date               =post['push_date']
        investor.new_investor            =post['new_investor']
        investor.new_natural_person      =post['new_natural_person']
        investor.new_non_natural_person  =post['new_non_natural_person']
        investor.final_investor          =post['final_investor']
        investor.final_natural_person    =post['final_natural_person']
        investor.final_non_natural_person=post['final_non_natural_person']
        return investor

class ShiborRate(models.Model):
    """
    Shibor 利率
    """
    push_date  =models.DateField(help_text="发布时间",primary_key=True)
    one_night  =models.DecimalField(help_text="隔夜利率",max_digits=16,decimal_places=4)
    one_week   =models.DecimalField(help_text="一周利率",max_digits=16,decimal_places=4)
    two_week   =models.DecimalField(help_text="两周利率",max_digits=16,decimal_places=4)
    one_month  =models.DecimalField(help_text="一月利率",max_digits=16,decimal_places=4)
    three_month=models.DecimalField(help_text="三月利率",max_digits=16,decimal_places=4)
    six_month  =models.DecimalField(help_text="六月利率",max_digits=16,decimal_places=4)
    nine_month =models.DecimalField(help_text="九月利率",max_digits=16,decimal_places=4)
    one_year   =models.DecimalField(help_text="一年利率",max_digits=16,decimal_places=4)

    @classmethod
    def fromPostInit(cls,post):
        """
        从POST发来的数据初始化一个ShiborRate 实例
        """
        shibor            =ShiborRate()
        shibor.push_date  =post['push_date']
        shibor.one_night  =post['one_night']
        shibor.one_week   =post['one_week']
        shibor.two_week   =post['two_week']
        shibor.one_month  =post['one_month']
        shibor.three_month=post['three_month']
        shibor.six_month  =post['six_month']
        shibor.nine_month =post['nine_month']
        shibor.one_year   =post['one_year']
        return shibor

class StockIndex(models.Model):
    """
    记录股指信息
    """
    push_date   =models.DateField(help_text="发布时间")
    index_name  =models.CharField(help_text="指数名",max_length=16)
    open_value  =models.DecimalField(help_text="开盘",max_digits=16,decimal_places=4,default=0)
    close_value =models.DecimalField(help_text="收盘",max_digits=16,decimal_places=4,default=0)
    higest_value=models.DecimalField(help_text="最高",max_digits=16,decimal_places=4,default=0)
    lowest_value=models.DecimalField(help_text="最低",max_digits=16,decimal_places=4,default=0)
    fluctuation =models.DecimalField(help_text="涨跌幅",max_digits=16,decimal_places=4,default=0)
    transaction_amount=models.DecimalField(help_text="成交金额",max_digits=20,decimal_places=4,default=0)
    total_market_value=models.DecimalField(help_text="总市值",max_digits=20,decimal_places=4,default=0)
    circulation_market_value=models.DecimalField(help_text="流通市值",max_digits=20,decimal_places=4,default=0)
    spe         =models.DecimalField(help_text="静态市盈率",max_digits=16,decimal_places=4,default=0)
    dpe         =models.DecimalField(help_text="动态市盈率",max_digits=16,decimal_places=4,default=0)
    pb          =models.DecimalField(help_text="市净率",max_digits=16,decimal_places=4,default=0)
    dp          =models.DecimalField(help_text="股息率",max_digits=16,decimal_places=4,default=0)
    lyspe       =models.DecimalField(help_text="去年底静态市盈率",max_digits=16,decimal_places=4,default=0)
    lydpe       =models.DecimalField(help_text="去年底动态市盈率",max_digits=16,decimal_places=4,default=0)
    lypb        =models.DecimalField(help_text="去年底市净率",max_digits=16,decimal_places=4,default=0)

    class Meta:
        unique_together=('push_date','index_name')

    @classmethod
    def add_or_update_and_save_stock_index_info(cls,post):
        """
        新增或是对已有的数据进行更新
        """
        target_row=None
        try:
            target_row=cls.objects.get(models.Q(push_date=post['push_date']),models.Q(index_name=post['index_name']))

        except cls.DoesNotExist as e:
            #进入到这个说明没有数据，那么就创建一个新行
            stock=cls()
            for k in post:
                if k not in ['push_date','index_name']:
                    stock[k]=post[k]
            stock.save()
            return "ok data been inserted"
        except Exception as e:
            em="warn exception in market.models.add_or_update_stock_index_info : {0}".format(e)
            return em
        if target_row != None:
            #如果进入到这个逻辑，那么说数据已经有了
            for k in post:
                if k not in ['push_date','index_name']:
                    target_row[k]=post[k]
            target_row.save()
        return "ok data been inserted"


        



