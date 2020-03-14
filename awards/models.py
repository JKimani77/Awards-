# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
 
class Profile(models.Model):
    '''
    Profile model and methods associated
    '''
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50)
    profile_photo =models.CloudinaryField(blank = True, null = True)
    bio = models.TextField(max_length = 150)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name = '')
    contact_phonenumber = models.IntegerField(blank = True, null = True)
    contact_email = models.EmailField

    def save_profile(self):
        '''save user profile'''
        self.save()

    def del_profile(self):
        '''delete user profile'''
        self.delete()

    @classmethod
    def get_profile_id(cls, id):
        profile = cls.objects.filter(id=id).all()
        return profile

    def update_profile(self, about):
        self.about = about
        self.save()

