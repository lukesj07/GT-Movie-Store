from django.contrib.auth.forms  import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join({
            f'<div class="alert alert-danger" role-"alert"> {e}</div>' for e in self
        }))

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form_control'}
            )

class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=150)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'new_password', 'confirm_password']:
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        # Validate that user exists
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError('Username does not exist.')

        # Validate password match
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise ValidationError('Passwords do not match.')
