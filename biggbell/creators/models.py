from django.db import models
from userauth.models import Creator , Brand
# Create your models here.

class CreatorInbox(models.Model):
    creator = models.ForeignKey(to=Creator, on_delete=models.CASCADE , related_name='creatorInbox')
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE , related_name='creatorInbox')
    email = models.EmailField(max_length=255)
    file = models.FileField(upload_to='creatorInbox',default=None)
    description = models.TextField()
    isseen = models.BooleanField(default=False)
