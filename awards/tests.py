# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Project,Profile,Review
from django.contrib.auth.models import User



class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user_stan = User(username='stann',email='stann@gmail.com', password='abcdef')
        self.second_profile = Profile(profile_pic='/path/image.png',user=self.user_stann, bio= 'I am groot',contact_phonenumber='0712345678', contact_email='stann@gmail.com')
        
        
    def test_save_profile(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        profiley = Profile.objects.all()
        self.assertTrue(len(profiley) > 0)
    
    def test_delete_profile(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        self.second_profile.delete_profile()
        profiley = Profile.objects.all()
        self.assertTrue(len(profiley)== 0)
        
    def test_update_profile(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        self.second_profile.get_profile_id(self.second_profile.id)
        self.second_profile.update_profile('This is an updated bio')
        self.assertTrue(self.second_profile.bio=='This is an updated bio')
        
    def test_get_prof_id(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        self.second_profile.get_profile_id(self.second_profile.id)
        profiley = Profile.objects.all()
        self.assertTrue(len(profiley) > 0)
        
