from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email непременно должен быть указан')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ExtUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        'Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    firstname = models.CharField(
        'Имя/Наименование',
        max_length=50,
        null=True,
        blank=True
    )
    register_date = models.DateField(
        'Дата регистрации',
        auto_now_add=True
    )
    mobile = models.CharField(
        'Мобильный телефон',
        max_length=50,
        validators=[RegexValidator(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', "Мобильный телефон имеет неверный формат")],
        default='',
    )
    skype = models.CharField(
        'Логин Skype',
        max_length=32,
        default=''
    )
    user_type_select = (
        (0, 'Частное лицо'),
        (1, 'Компания'),
    )
    user_type = models.IntegerField(
        'Тип пользователя',
        choices=user_type_select,
        default=0
    )

    rate = models.IntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        'Активен',
        default=True
    )
    is_admin = models.BooleanField(
        'Суперпользователь',
        default=False
    )

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.email

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Avatar(models.Model):
    user = models.ForeignKey(ExtUser, default='', verbose_name='Пользователь')
    file = models.ImageField("Аватар", upload_to='images/avatars', help_text='Форматы: png, jpg, jpeg, bmp. gif')

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватар'