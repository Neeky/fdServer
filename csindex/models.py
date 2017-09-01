from django.db import models

# Create your models here.
class IndexOverview(models.Model):
    pushDate=models.DateTimeField()
    indexName=models.CharField(help_text='指数名',max_length=8)
    spe=models.DecimalField(max_digits=10,decimal_places=6)
    dpe=models.DecimalField(max_digits=10,decimal_places=6)
    pb =models.DecimalField(max_digits=10,decimal_places=6)
    dp =models.DecimalField(max_digits=10,decimal_places=6)

