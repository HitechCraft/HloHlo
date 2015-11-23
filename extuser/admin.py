from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import ExtUser


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'firstname',
        'is_admin',
    ]

    list_filter = ('is_admin',)

    fieldsets = (
                (None, {'fields': ('email',)}),
                ('Personal info', {
                 'fields': (
                    'firstname',
                    'user_type',
                    'mobile',
                    'skype',
                 )}),
                ('Permissions', {'fields': ('is_admin',)}),
                ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'firstname',
                'user_type',
                'mobile',
                'skype',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Регистрация нашей модели
admin.site.register(ExtUser, UserAdmin)
admin.site.unregister(Group)