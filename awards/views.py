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
from .forms import ProfileForm, ProjectsForm, ReviewForm
from .serializer import ProjectsSerializer, ProfileSerializer
from .permissions import IsAdminOrReadOnly

from django.conf import settings
import os
# Create your views here.
def index(request):
    '''
    view fuction to display landing page
    '''
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
    profile = Profile.objects.filter(user_id = id).all()
    projects = Projects.objects.filter(profile=current_user.id).all()
    return render(request, 'profile.html', {"profile":profile, "projects":projects})

def post(request):
    '''
    view function to render a form to post projects
    '''
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

def search(request):
    '''
    view function to search by project titles
    '''
    if 'project' in request.GET and request.GET['project']:
        search_proj = request.GET.get('project')
        projects_searched = Projects.searchproject(search_proj)
        message = f'{search_proj}'
        return render(request, 'search.html',{"projects":projects_searched, "message":message})

def rate(request, id):
    '''
    view function to render the review form
    '''
    current_user = request.user
    project = Projects.objects.get(pk=id)
    reviews = Rating.objects.filter(project=project.id).all()
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = current_user
            review.project = project
            review.save_review()
            # alert("Your response has been recorded")
            return redirect(index)
        
    else:
        form = ReviewForm()
    return render(request, 'reviewform.html', {"form":form, "project":project, "reviews":reviews}) 

def rated(request, id):
    project = Projects.objects.get(pk=id)
    ratings = Rating.objects.filter(project=project.id).all()
    design = Rating.objects.filter(project=project.id).values_list('design',flat=True)
    usability = Rating.objects.filter(project=project.id).values_list('usability',flat=True)
    content = Rating.objects.filter(project=project.id).values_list('content',flat=True)
    total_d=0
    total_u=0
    total_c = 0
    for score in design:
        total_d+=score
    for score in usability:
        total_u+=score
    for score in content:
        total_c+=score
        
        
    average = (total_d + total_u + total_c)/3
    return render(request, 'review.html',{"project":project, "ratings":ratings,"total_score":average}) 

class ProjectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    # def post(self, request, format=None):
    #     serializers = ProjectsSerializer(data=request.data)
        
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data, status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        



# token by postman after creating post method   "token": "555f67e0f9575a9f5ac3f09822c4c4e8ee30bd26"
#555f67e0f9575a9f5ac3f09822c4c4e8ee30bd26
