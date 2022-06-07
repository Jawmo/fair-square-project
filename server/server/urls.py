from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from transaction_emails.views import send_email_with_template, postmark_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/', send_email_with_template, name="send_email"),
    path('postmark_webhook/', csrf_exempt(postmark_webhook), name="postmark_webhook"),
]

# Additional paths/routes could be created to allow non-developers to reach version information
# or providing login access to an admin panel that visualizes the data as needed.