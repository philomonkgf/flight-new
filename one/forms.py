from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import NewUser


class SingupUser(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['email','username','first_name','last_name','bio']