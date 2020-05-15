from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from captcha.fields import CaptchaField
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	
    #captcha = CaptchaField()
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
	
    #captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ('email',)