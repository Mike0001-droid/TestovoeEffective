from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import (
    AdminPasswordChangeForm
)
from account.forms import UserChangeForm, UserCreationForm
from account.models import MyUser


class UserAdmin(BaseUserAdmin):
    # Формы для добавления и изменения пользовательских экземпляров
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    # Поля, которые будут использоваться при отображении модели пользователя.
    # Они переопределяют определения в базовом User Admin,
    # которые ссылаются на определенные поля в auth.User.
    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')})
    )
    # add_fieldsets не является стандартным атрибутом ModelAdmin. UserAdmin
    # переопределяет get_fieldsets, чтобы использовать этот атрибут при создании пользователя.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('user_permissions',)


admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
