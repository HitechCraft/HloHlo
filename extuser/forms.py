from urllib import request
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import FormView
from multiupload.fields import MultiFileField
from extuser.models import ExtUser


class UserCreationForm(forms.ModelForm):

    firstname = forms.CharField(
        label='Имя/Наименование',
        error_messages={'required': 'Введите ваше имя'},
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    email = forms.EmailField(
        error_messages={'required': 'Введите email'},
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    password1 = forms.CharField(
        label='Пароль',
        error_messages={'required': 'Введите пароль'},
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label='Подтверждение',
        error_messages={'required': 'Введите подтверждение пароля'},
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    mobile = forms.CharField(
        label='Мобильный телефон',
        error_messages={'required': 'Введите номер телефона'},
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    skype = forms.CharField(
        label='Логин Skype',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    attachments = MultiFileField(label="Выберите фото", max_num=1, max_file_size=1024*1024*5, required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'firstname', 'user_type', 'mobile', 'skype')


class UserChangeForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['firstname', 'mobile', 'skype']


class UserChangePasswordForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Пароль',
        error_messages={'required': 'Введите пароль'},
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Подтверждение',
        error_messages={'required': 'Введите подтверждение пароля'},
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')

        return password2

    def save(self, commit=True):
        user = super(UserChangePasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password1', 'password2']


class LoginForm(forms.Form):

    email = forms.EmailField(
        error_messages={'required': 'Введите Email'},
    )
    
    password = forms.CharField(
        error_messages={'required': 'Введите пароль'},
        widget=forms.PasswordInput
    )

    def login(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)