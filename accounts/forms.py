from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'date_of_birth', 'username', 'email')
        widgets = {
            'my_date': DateInput()
        }
class CustomUserAuthForm(AuthenticationForm):
    captcha = CaptchaField()
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

