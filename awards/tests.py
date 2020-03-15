# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Projects, Profile, Rating
from django.contrib.auth.models import User



class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user_stann = User(username='stann',email='stann@gmail.com', password='abcdef')
        self.second_profile = Profile(profile_pic='/path/image.png',user=self.user_stann, bio= 'I am groot',contact_phonenumber='0712345678')
        
        
    def test_save_profile(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        profiley = Profile.objects.all()
        self.assertTrue(len(profiley) > 0)
    
    def test_delete_profile(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        self.second_profile.del_profile()
        profiley = Profile.objects.all()
        self.assertTrue(len(profiley)== 0)
        
    def test_update_profile(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        self.second_profile.update_profile(self.second_profile.bio)
        self.second_profile.update_profile('This is an updated bio')
        self.assertTrue(self.second_profile.bio=='This is an updated bio')
        
    def test_get_profile_id(self):
        self.user_stann.save()
        self.second_profile.save_profile()
        self.second_profile.get_profile_id(self.second_profile.id)
        profiley = Profile.objects.all()
        self.assertTrue(len(profiley) > 0)
        
class ProjectsModelTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    def setUp(self):
        self.user_one = User(username='stunn', email='stunn@gmail.com', password='123456')
        self.profile_one = Profile(profile_pic='path/image.png',user=self.user_one, bio="Ola,ola,ola,ola,ola,ola,ola,ola",contact_phonenumber='0712345678')
        self.project_one = Projects(title='FOOTSUBISHI', description='Project one', project_url='/path/screenshot.png',profile=self.profile_one)
        
        
    def test_save_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save_project()
        
        projectz = Projects.objects.all()
        self.assertTrue(len(projectz)>0)

    def test_delete_project(self):
        self.user_one.save()
        self.profile_one.save_profile()
        self.project_one.save_project()
        self.project_one.delete_project()
        projectz = Projects.objects.all()
        self.assertTrue(len(projectz)== 0)
    
    def test_update_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save()
        self.project_one.get_project_id(self.project_one.id)
        self.project_one.update_project('OMI WIO WAM NAO')
        self.assertTrue(self.project_one.title=='OMI WIO WAM NAO')
        
    def test_get_project_id(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save()
        self.project_one.get_project_id(self.project_one.id)
        projectz = Projects.objects.all()
        self.assertTrue(len(projectz)> 0)

    def test_search(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save_project()

        projectz = self.project_one.search_by_project('FOOTSUBISHI')
        self.assertTrue(len(projectz) > 0)

       
    
    
    


