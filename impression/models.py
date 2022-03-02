from django.db import models
from django.utils import timezone

class Evaluation(models.Model):
    eval = models.CharField('番号',max_length=255,null=True,blank=True)

    def __str__(self):
        return self.eval


class Impression(models.Model):
    GENDER = (
        ('男','男'),
        ('女','女'),
        ('その他','その他')
    )

    name = models.CharField('お名前',max_length=255)
    age = models.IntegerField('年齢',default=20)
    gender = models.CharField('性別',choices=GENDER,max_length=10)
    pattern1 = models.IntegerField('パターン１',default=1)
    pattern2 = models.IntegerField('パターン２',default=1)
    pattern3 = models.IntegerField('パターン３',default=1)
    pattern4 = models.IntegerField('パターン４',default=1)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.name