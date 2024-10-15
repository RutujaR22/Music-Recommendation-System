from django.db import models
# Create your models here.


## database for quiz
class quiz(models.Model):
    question=models.CharField(max_length=200,null=True,blank=True)
    op1=models.CharField(max_length=200,null=True,blank=True)
    op2=models.CharField(max_length=200,null=True,blank=True)
    op3=models.CharField(max_length=200,null=True,blank=True)
    op4=models.CharField(max_length=200,null=True,blank=True)
    op5=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.question

## database for dataset
class dataset(models.Model):
    option=models.CharField(max_length=2000,null=True)
    emotion=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.option
class mood(models.Model):
    user = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    mymood = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.mymood