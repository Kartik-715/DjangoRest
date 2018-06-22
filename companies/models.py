from django.db import models

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open1 = models.FloatField()
    close = models.FloatField() 
    Volume = models.IntegerField()


    def __str__(self):
        return self.ticker   


