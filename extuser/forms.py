from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.views.generic import FormView


class UserCreationForm(forms.ModelForm):

    first_name = forms.CharField(
        label='Имя',
        error_messages={'required': 'Введите ваше имя'}
    )

    email = forms.EmailField(
        error_messages={'required': 'Введите email'}
    )

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

    mobile = forms.CharField(
        label='Мобильный телефон',
        error_messages={'required': 'Введите номер телефона'},
    )

    skype = forms.CharField(
        label='Логин Skype',
        required=False
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

    class Meta:
        model = get_user_model()
        fields = ('email', 'firstname', 'mobile', 'skype')


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/users/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class UserChangeForm(forms.ModelForm):

    """Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя."""

    password1 = forms.CharField(
        label='Пароль',
        required=False,
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Подтверждение пароля',
        required=False,
        widget=forms.PasswordInput
    )

    mobile = forms.CharField(
        required=False
    )

    skype = forms.CharField(
        required=False
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        if self.clean_password2():
            user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['firstname', 'mobile', 'skype']


class UserChangeFormView(FormView):
    form_class = UserChangeForm
    success_url = "/users/edit/"
    template_name = "edit.html"

    def form_valid(self, form):
        form.save()
        return super(UserChangeFormView, self).form_valid(form)


class LoginForm(forms.Form):

    """Форма для входа в систему
    """
    email = forms.EmailField(
        error_messages={'required': 'Введите Email'},
    )
    
    password = forms.CharField(
        error_messages={'required': 'Введите пароль'},
    )


class LoginFormView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form):
        form.save()
        return super(LoginFormView, self).form_valid(form)
