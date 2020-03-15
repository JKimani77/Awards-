# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Projects, Profile, Rating
from .forms import ProfileForm
from .serializer import ProjectsSerializer


from django.conf import settings
import os
# Create your views here.
def index(request):
    projects = Projects.get_project()
    return render(request, 'home.html', {"projects":projects})

@login_required(login_url='login/')
def profile(request):
    '''
    function to create/update user profile
    '''
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user 
            profile.save()
            return redirect(profile_user)
    else:
        form = ProfileForm()
    return render(request, 'createprofile.html',{"form":form})


@login_required(login_url='login/')
def profile_user(request, id):
    '''
    funcion to display user profile
    '''
    current_user = request.user
    profile = Profile.objects.filter(user_id=id).all()
    projects = Projects.objects.filter(profile=current_user.id).all()
    return render(request, 'profile.html', {"profile":profile, "projects":projects})

class ProjectsList(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        return Response(serializers.data)