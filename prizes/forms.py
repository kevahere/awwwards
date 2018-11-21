from django import forms
from .models import Profile, Project, Ratings

class UpdateProfile(forms.ModelForm):
    """Enables the user to update their bio and profile pic"""
    class Meta:
        model =Profile
        exclude = ['user']

class PostProjectForm(forms.ModelForm):
    """Enabling the user to upload projects"""
    class Meta:
        model = Project
        exclude = ['user','post_date', 'likes']

class RatingsForm(forms.ModelForm):
    """Enables user to comment on images"""
    class Meta:
        model = Ratings
        exclude = ['user','pub_time', 'image']