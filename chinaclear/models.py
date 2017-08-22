from django.db import models

# Create your models here.
class InvestorOverview(models.Model):
    newlyAddInvestors=models.DecimalField(max_digits=16,decimal_places=6)
    endInvestors     =models.DecimalField(max_digits=16,decimal_places=6)
    pushDate         =models.DecimalField(max_digits=16,decimal_places=6)
