

from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.forms import forms

from django.contrib.auth.forms import PasswordChangeForm


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for fieldname in ['new_password1','new_password2']:
            self.fields[fieldname].widget.attrs ={"class":'form-control'}