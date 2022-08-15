from django.db import models

# Create your models here.
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)'''
        

class User(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    hakbu = models.CharField(max_length=20, blank=True, null=True)
    hakgwa = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'

class Dasan(models.Model):
    dasan_no = models.AutoField(primary_key=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dasan'