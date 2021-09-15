from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions_on_top = False
    actions_on_bottom = True
    list_display = ('id', 'nickname', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_display_links = ('nickname', )
    list_editable = ('is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'groups')
    fields = ('nickname', 'username', 'email', 'groups', 'user_permissions', ('is_superuser', 'is_staff', 'is_active'))
    search_fields = ('nickname', 'username', 'email')
