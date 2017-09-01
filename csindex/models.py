from django.db import models

# Create your models here.
class IndexOverview(models.Model):
    pushDate=models.DateTimeField(primary_key=True)
    spe=models.DecimalField(max_digits=10,decimal_places=6)
    dpe=models.DecimalField(max_digits=10,decimal_places=6)
    pb =models.DecimalField(max_digits=10,decimal_places=6)
    dp =models.DecimalField(max_digits=10,decimal_places=6)

