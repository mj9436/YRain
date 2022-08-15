from django.db import models

# Create your models here.
class Record(models.Model):
    record_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=10)
    borrow_date = models.DateTimeField()
    borrow_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'record'


class User(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'


class Yangjae(models.Model):
    yangjae_no = models.AutoField(primary_key=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yangjae'



class Dasan(models.Model):
    dasan_no = models.AutoField(primary_key=True)
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dasan'
