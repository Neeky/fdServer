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

        



