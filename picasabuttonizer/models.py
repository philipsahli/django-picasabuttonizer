from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models
import uuid

# Create your models here.
class Button(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(User, blank=True, null=True)
    guid = models.CharField(max_length=50, unique=True)
    icon = models.FileField(upload_to="picasabuttonizer/icons")
    icon_name = models.CharField(max_length=30)
    label = models.CharField(max_length=100)
    tooltip = models.CharField(max_length=100)
    hybrid_uploader_url = models.URLField(verify_exists=False)

    def save(self, force_insert=False, force_update=False, using=None):
        self.guid = str(uuid.uuid1())
        super(Button, self).save(force_insert, force_update, using)

    def delete(self, using=None):
        self.icon.delete()
        super(Button, self).delete(using)

    def id(self):
        return self.user.username+"/{"+self.guid+"}"



