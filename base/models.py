from django.db import models
from django.contrib.auth.models import AbstractUser

class User( AbstractUser ):
    role = models.CharField(max_length=100, default="admin")
    submitted = models.BooleanField( default=False )

class StudentFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3 = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    q5 = models.IntegerField(default=0)
    q6 = models.IntegerField(default=0)
    

class WorkerFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3 = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    

class Shanghai(models.Model):
    subject = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    ranking = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return f"{self.subject} {self.year}"

class QS(models.Model):
    subject = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    ranking = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return f"{self.subject} {self.year}"

class Webometrics(models.Model):
    subject = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    ranking = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return f"{self.subject} {self.year}"
    
class THE(models.Model):
    subject = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    ranking = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return f"{self.subject} {self.year}"

'''
dave
dave@email.com
1!2@3#4$5%6^
'''