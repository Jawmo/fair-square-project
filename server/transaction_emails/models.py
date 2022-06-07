from django.db import models
from core.models import BaseModel
from django.conf import settings

# If we wanted to tally the number of clicks or opens instead, we could make the field
# an integer and increment the amount.

# We could also potentially also save the datetime of the first open and first click
# to register how soon the emails were being interacted with.

class EmailVersion(BaseModel):
    
    # id auto created as PK for table
    version_alias = models.CharField(null=False, blank=False, max_length=8)
    email_alias = models.CharField(blank=False, null=False, max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    postmark_template_id = models.IntegerField(blank=False)
    changes = models.TextField()
    total_opened = models.IntegerField() # tracking all clicks from this version
    total_link_clicks = models.IntegerField() # tracking all clicks from this version

    class Meta:
        verbose_name = "Email Version"
        ordering = ["-created_date"]

    def __str__(self):
        return self.version_alias

class TransactionEmail(BaseModel):

    # id auto created as PK for table
    version = models.ForeignKey(EmailVersion, blank=False, null=False, on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    to_email = models.CharField(blank=False, null=False, max_length=50)
    opened = models.BooleanField(blank=False, null=False, default=False)
    link_clicked = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        verbose_name = "Transaction Email"
        ordering = ["-created_date"]
        
    

