from django import forms
from .models import Profile, Posts, Comment
from django.utils.safestring import mark_safe



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'onchange': 'previewImage(event)'})
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
            'placeholder': 'Title'
        })
            }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']