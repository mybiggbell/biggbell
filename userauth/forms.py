from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField
from .models import  MyUser , Creator ,Brand
from django.utils.translation import gettext, gettext_lazy as _
 

class UserRegistration(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = MyUser
        fields = ('email','first_name','last_name','contact_number','password1','password2','gender','country_name')

        widgets = {'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'contact_number':forms.NumberInput(attrs={'class':'form-control'}),
                    'password1':forms.TextInput(attrs={'class':'form-control'}),
                    'password2':forms.TextInput(attrs={'class':'form-control'}),
                    'gender':forms.Select(attrs={'class':'form-control'}),
                    'country_name':forms.TextInput(attrs={'class':'form-control'})
            }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.EmailInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))



class CreatorFrom(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ('profile_img','youtube_name','instagram_name','youtube_link','instagram_link','linkedin_link','type_of_youtube','youtube_subscriber','instagram_followers','low_Budget','high_Budget')
        widgets = { 
                    'profile_img':forms.FileInput(attrs={'class':'form-control'}),
                    'youtube_name':forms.TextInput(attrs={'class':'form-control'}),
                    'instagram_name':forms.TextInput(attrs={'class':'form-control'}),
                    'youtube_link':forms.URLInput(attrs={'class':'form-control'}),
                    'instagram_link':forms.URLInput(attrs={'class':'form-control'}),
                    'linkedin_link':forms.URLInput(attrs={'class':'form-control'}),
                    'type_of_youtube':forms.TextInput(attrs={'class':'form-control'}),
                    'youtube_subscriber':forms.NumberInput(attrs={'class':'form-control'}),
                    'instagram_followers':forms.NumberInput(attrs={'class':'form-control'}),
                    'low_Budget':forms.NumberInput(attrs={'class':'form-control'}),
                    'high_Budget':forms.NumberInput(attrs={'class':'form-control'}),
            }
        

class BrandFrom(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('company_name','company_profile_link','company_official_email')
        widgets = { 
                     
                    'company_name':forms.TextInput(attrs={'class':'form-control'}),
                    'company_profile_link':forms.URLInput(attrs={'class':'form-control'}),
                    'youtube_subscriber':forms.NumberInput(attrs={'class':'form-control'}),
                    'company_official_email':forms.EmailInput(attrs={'class':'form-control'})
            }
        
         
         

         