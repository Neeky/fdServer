from django.db import models

# Create your models here.

class MarketOverview(models.Model):
    totalValue=models.DecimalField(max_digits=16,decimal_places=4,default=0,help_text='A股总市值')
    circulationValue=models.DecimalField(max_digits=16,decimal_places=4,default=0,help_text='流通市值')
    tradValue=models.DecimalField(max_digits=16,decimal_places=4,default=0,help_text='成交金额')
    turnoverRate=models.DecimalField(max_digits=16,decimal_places=4,default=0,help_text='换手率')
    PERate=models.DecimalField(max_digits=16,decimal_places=4,default=0,help_text='平均市盈率')
    pushDate=models.DateTimeField(primary_key=True,help_text='发布时间')
