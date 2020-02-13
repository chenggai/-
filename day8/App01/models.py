from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = 'bbs_user'
        #表名对应的中文名
        verbose_name_plural='用户'

