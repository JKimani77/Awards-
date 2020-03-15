# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Projects, Profile, Rating

from django.conf import settings
import os
# Create your views here.
def index(request):
    projects = Projects.get_project()
    return render(request, 'home.html', {"projects":projects})
