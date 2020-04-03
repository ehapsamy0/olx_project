from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=(forms.EmailInput(attrs={'class':'come_class'})))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('phone','address','user_img')



class EditUserDate(forms.Form):
    first_name = forms.CharField(max_length=50,required=False,help_text='First_name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=(forms.EmailInput(attrs={'class':'come_class'})))
    phone = forms.CharField(max_length=30, required=False, help_text='Optional.')
    address = forms.CharField(max_length=253,required=False, help_text='Optional.')
    user_img = forms.ImageField()