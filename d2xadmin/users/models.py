from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="", max_length=8)
    address = models.CharField(max_length=100, default="")
    moblie = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/defaut.png", max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username