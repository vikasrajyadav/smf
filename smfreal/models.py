from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

#create your models

class fundlist(models.Model):
    fundno = models.CharField(max_length=200,unique=True,primary_key=True)
    fundcompany = models.CharField(max_length=200)
    fundtype = models.CharField(max_length=200)
    fundname = models.CharField(max_length=200)
    fundlaunchdate = models.CharField(max_length=200)
    fundreturn_1 = models.CharField(max_length=200,null=True)
    fundreturn_2 = models.CharField(max_length=200,null=True)
    fundreturn_3 = models.CharField(max_length=200,null=True)
    fundreturn_5 = models.CharField(max_length=200,null=True)
    fundrating = models.CharField(max_length=200,null=True)
    fundrisk = models.CharField(max_length=200,null=True)
    fundminimumSIP = models.CharField(max_length=200,null=True)
    fundminimumInvest = models.CharField(max_length=200,null=True)
    fundexpenseratio = models.CharField(max_length=200,null=True)
    fundNAV = models.CharField(max_length=200,null=True)
    fundportfolio = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.fundno

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30,null=True)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank='True')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('smfreal.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Myuserdb(models.Model):
    myusername = models.CharField(max_length=20,unique=True)
    user_full_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200,null=True)
    user_pan_card = models.CharField(max_length=200)
    user_bank_ifsc = models.CharField(max_length=200)
    user_bank_account_no = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now())
    # published_date = models.DateTimeField(blank=True,null=True)
    #
    # def user_created(self):
    #     self.published_date = timezone.now()
    #     self.save()

    #
    # def get_absolute_url(self):
    #     return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.myusername
