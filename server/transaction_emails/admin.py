from django.contrib import admin
from .models import TransactionEmail, EmailVersion

class TransactionEmailAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('version', 'to_user', 'opened', 'link_clicked',)
        }),
    )
    list_display = ['version', 'to_user', 'opened', 'link_clicked',]
    readonly_fields=('created_date', 'id')
    ordering=('-created_date',)

class EmailVersionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('version_alias', 'email_alias', 'postmark_template_id', 'author', 'changes', 'total_opened', 'total_link_clicks',)
        }),
    )
    list_display = ['version_alias', 'email_alias', 'postmark_template_id', 'author', 'changes', 'total_opened', 'total_link_clicks',]
    readonly_fields=('created_date', 'id')
    ordering=('-created_date',)

admin.site.register(TransactionEmail, TransactionEmailAdmin)
admin.site.register(EmailVersion, EmailVersionAdmin)