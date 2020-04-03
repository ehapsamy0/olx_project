from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save,post_save
import os
import random

# Create your models here.



def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'user_images/{userid}/{basename}{ext}'.format(userid=instance.user.id,
                                                                             basename=basefilename,
                                                                             randomstring=randomstr, ext=file_extension)


class User_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True,null=True)
    address = models.CharField(blank=True,null=True,max_length=400)
    user_img = models.ImageField(upload_to=photo_path,blank=True,null=True)



    def __str__(self):
        return self.user.username



