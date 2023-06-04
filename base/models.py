from django.db import models
from django.contrib.auth.models import AbstractUser

class User( AbstractUser ):
    full_name = models.CharField(max_length = 200, default="Fakhri")
    submitted = models.BooleanField(default=False)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # questiopns Lists
    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3 = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    q5 = models.IntegerField(default=0)
    q6 = models.IntegerField(default=0)
    q7 = models.IntegerField(default=0)
    q8 = models.IntegerField(default=0)
    q9 = models.IntegerField(default=0)
    q10 = models.IntegerField(default=0)
    q11 = models.IntegerField(default=0)



'''
dave
dave@email.com
1!2@3#4$5%6^
'''