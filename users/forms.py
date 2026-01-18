from django.contrib.auth.models import User, Group,Permission
from django import forms
from django.core.exceptions import ValidationError
from events.forms import FormMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUserModel
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm

User = get_user_model()

class CustomRegistrationForm(FormMixin, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password', 'email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exist = User.objects.filter(email=email).exists()

        if email_exist:
            raise forms.ValidationError('This Email is Already Exist')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        errors = []

        if len(password) < 8:
            errors.append('Password Must be Included 8 Character')

        if ('$' not in password) and ('#' not in password) and ('@' not in password):
            errors.append('Password Must Be Included $ or @ or #')

        if errors:
            raise forms.ValidationError(errors)

        return password

    def clean(self):
        cleaned_datas = super().clean()
        password = cleaned_datas.get('password')
        confirm_password = cleaned_datas.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password do not matched')
        else:
            return cleaned_datas


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()


class LoginForm(FormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()


class AssignRoleForm(FormMixin, forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label='Select a role'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()


class CreateGroupForm(FormMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset = Permission.objects.all(),
        widget= forms.CheckboxSelectMultiple,
        required=False,
        label='Create a new group'
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()

class EditProfileForm(FormMixin,forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['first_name', 'last_name', 'profile_picture', 'bio', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()

class CustomPasswordChangeForm(FormMixin, PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        self.apply_class()


class CustomPasswordResetForm(FormMixin,PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()


class CustomPasswordResetConfirmForm(FormMixin,SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.apply_class()