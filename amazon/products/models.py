from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=230)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=700)

    class Meta:
        db_table='anoop'

