from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        labels = {
            'username':'Username',
            'email': 'Email Address',
            'password1':'Password',
            'password2':'Password Confirmation'
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'slug')

        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'social_twitter':'Twitter Account',
            'social_facebook':'Facebook Account',
            'social_linkedin':'Linkedin Account',
            'social_youtube':'Youtube Account',
            'social_instagram':'Instagram Account',
            'social_whatsapp':'WhatsApp Account'
        }
