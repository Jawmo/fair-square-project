from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser, BaseModel):

    # id auto created as PK for table
    email = models.CharField(blank=False, null=False, max_length=75) # email used as username
    name = models.CharField(blank=False, null=False, max_length=50)
    
    # perhaps adding a 'lifetime_emails_opened' or 'lifetime_links_clicked' to track how engaged 
    # the user is over time?
    
