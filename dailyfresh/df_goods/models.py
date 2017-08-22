from django.db import models

# Create your models here.
class Goods(models.Model):
    goods_name = models.CharField(max_length=20)
    goods_price = models.DeciamlField(max_digits=10, decimal_places=2)
