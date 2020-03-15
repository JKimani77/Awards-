# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import cloudinary
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
 
class Profile(models.Model):
    '''
    Profile model and methods associated
    '''
    profile_pic = CloudinaryField(blank = True, null = True)
    bio = models.TextField(max_length = 550)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_phonenumber = models.IntegerField(blank = True, null = True)
    

    def save_profile(self):
        '''save user profile'''
        self.save()

    def del_profile(self):
        '''delete user profile'''
        self.delete()
    
    def update_profile(self, bio):
        self.bio = bio
        self.save()

    @classmethod
    def get_profile_id(cls, id):
        profile = cls.objects.filter(id=id).all()
        return profile

class Projects(models.Model):
    '''
    A model containing the project image and 
    description columns and the methods associated
    with the model
    '''
    title = models.CharField(max_length=50)
    project_image = CloudinaryField(null=True)
    description = models.TextField(max_length=250)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null=True)
    project_url = models.URLField(null=True)


    def save_project(self):
        '''save an image in database'''
        self.save()

    def delete_project(self):
        '''delete image from the database'''
        self.delete()
    
    def update_project(self, title):
        self.title = title
        self.save()

    @classmethod
    def get_project(cls):
        projectz = cls.objects.all()
        return projectz

    @classmethod
    def get_project_id(cls, id):
        projectz = cls.objects.filter(id=id).all()
        return projectz

    @classmethod
    def search_by_project(cls, search_term):
        projectz = cls.objects.filter(title__icontains=search_term)
        return projectz

class Rating(models.Model):
    design = models.IntegerField()
    content = models.IntegerField()
    review = models.TextField(max_length = 500)
    usability = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project =  models.ForeignKey(Projects, on_delete = models.CASCADE)
    totalscore =  models.IntegerField()


    def save_review(self):
        self.save()


## will not create review class because it's defined as a column from the Rating model
#related name on User columns (Profile, Rating) omitted