from django.db import models
from datetime import datetime,date

# Create your models here.
class GlodPrice(models.Model):
    pushDate=models.DateTimeField(primary_key=True)
    contract=models.CharField(max_length=8)
    openingPrice=models.DecimalField(max_digits=10,decimal_places=6)
    closingPrice=models.DecimalField(max_digits=10,decimal_places=6)
    highestPrice=models.DecimalField(max_digits=10,decimal_places=6)
    minimumPrice=models.DecimalField(max_digits=10,decimal_places=6)
    
    def fromJson(self,jdt):
        dtn=datetime.now()
        dt=date(year=dtn.year,month=dtn.month,day=dtn.day)
        self.pushDate=dt
        self.contract=jdt['contract']
        self.openingPrice=jdt['openingPrice']
        self.closingPrice=jdt['closingPrice']
        self.highestPrice=jdt['highestPrice']
        self.minimumPrice=jdt['minimumPrice']
