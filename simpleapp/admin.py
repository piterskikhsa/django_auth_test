from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _

from simpleapp.forms import SimpleUserCreationForm, SimpleUserChangeForm
from simpleapp.models import SimpleUser


@admin.register(SimpleUser)
class UserAdmin(admin.ModelAdmin):
    add_form = SimpleUserCreationForm
    form = SimpleUserChangeForm
    model = SimpleUser
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    # change_password_form = AdminPasswordChangeForm
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    list_display_links = ('email', )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
