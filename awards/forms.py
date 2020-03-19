from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Projects, Rating

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'contact_phonenumber')

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'project_image', 'description', 'project_url' )