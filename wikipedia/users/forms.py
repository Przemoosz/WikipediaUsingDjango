from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, ProfilePrivacy


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, help_text=mark_safe('<p>&bull; E-Mail is not required but its recomended</p>'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    # nam = forms.CharField()
    # nam.widget,
    class Meta:
        model = Profile
        #fields = ['username']
        fields = ['Name',
                  'surname',
                  'gender',
                  'Age',
                  'semestr',
                  'kierunek',
                  'bio',
                  ]
class UserPrivacyForm(forms.ModelForm):
    class Meta:
        model = ProfilePrivacy
        fields = ['hidden_Age',]

