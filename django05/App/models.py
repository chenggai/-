from django.db import models

# Create your models here.
class User(models.Model):

    username=models.CharField(max_length=60,unique=True)
    password=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    phone=models.CharField(max_length=128)

    class Meta:   #表自身信息（元信息）
        db_table='user'



