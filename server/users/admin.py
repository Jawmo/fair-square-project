from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('id', 'username', 'name', 'email', 'created_date',)
        }),
        # ('Advanced options', {
        #     'classes': ('collapse',),
        #     'fields': ('registration_required', 'template_name'),
        # }),
    )
    list_display = ['id', 'username', 'name', 'email', 'created_date',]
    readonly_fields=('created_date', 'id')
    ordering=('-created_date',)

admin.site.register(CustomUser, CustomUserAdmin)