from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128, db_column='password_hash')

    class Meta:
        db_table = 'bbs_user'