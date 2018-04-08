from django.db import models
from django.utils import timezone
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

#create your models

class fundlist(models.Model):
    fundno = models.CharField(max_length=200,unique=True,primary_key=True)
    fundcompany = models.CharField(max_length=200)
    fundtype = models.CharField(max_length=200)
    fundname = models.CharField(max_length=200)
    fundlaunchdate = models.CharField(max_length=200)
    fundreturn = models.CharField(max_length=200)

    def __str__(self):
        return self.fundno

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    name = models.CharField(max_length=30,null=True)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank='True')

    def __str__(self):
        return self.user.username
