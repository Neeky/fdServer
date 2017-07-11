from django.db import models
from datetime import datetime
# Create your models here.

class MoneySupply(models.Model):
    pushDate=models.DateTimeField(primary_key=True)
    m0=models.DecimalField(max_digits=16,decimal_places=6)
    m1=models.DecimalField(max_digits=16,decimal_places=6)
    m2=models.DecimalField(max_digits=16,decimal_places=6)

    def fromJson(self,jdt):
        year,month=[int(v) for v in jdt['pushDate'].split('.')]
        self.pushDate=datetime(year,month,1)
        self.m0=jdt['m0']
        self.m1=jdt['m1']
        self.m2=jdt['m2']
 
