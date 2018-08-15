from django.db import models

class Transaction(models.Model):
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    quality = models.BooleanField()
    price = models.IntegerField()
    transaction_time = models.DateTimeField()
    buyer = models.CharField(max_length=21)
