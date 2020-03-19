# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Projects, Profile, Rating
from .forms import ProfileForm, ProjectsForm
from .serializer import ProjectsSerializer
from .permissions import IsAdminOrReadOnly

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
    profile = Profile.objects.get_profile_id(current_user.id).all()
    projects = Projects.objects.filter(profile=current_user.id).all()
    return render(request, 'profile.html', {"profile":profile, "projects":projects})

def post(request):
    current_user = request.user
    if request.method=="POST":
        form = ProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.profile = current_user.profile
            projects.save_project()
            return redirect(index)
    else:
        form = ProjectsForm()
    return render(request, 'postproject.html',{"form":form})

class ProjectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        



# token by postman after creating post method   "token": "555f67e0f9575a9f5ac3f09822c4c4e8ee30bd26"
#555f67e0f9575a9f5ac3f09822c4c4e8ee30bd26
