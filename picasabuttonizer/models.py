from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models
import uuid

class Button(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="name")
    user = models.ForeignKey(User, blank=True, null=True)
    guid = models.CharField(max_length=50, unique=True, null=True, blank=True)
    icon = models.FileField(upload_to="picasabuttonizer/icons")
    icon_name = models.CharField(max_length=30, null=True, blank=True)
    label = models.CharField(max_length=100)
    tooltip = models.CharField(max_length=100)

    #class Meta:
    #    abstract = True

    def save(self, force_insert=False, force_update=False, using=None):
        self.guid = str(uuid.uuid1())
        super(Button, self).save(force_insert, force_update, using)

    def delete(self, using=None):
        self.icon.delete()
        super(Button, self).delete(using)

    def id(self):
        return self.user.username+"/{"+self.guid+"}"

class HybridButton(Button):
    spec = models.URLField(verify_exists=False, max_length=30, verbose_name="URL of your Upload API")

class TrayexecButton(Button):
    spec = models.CharField(max_length=70, verbose_name="Path to command")

class OpenButton(Button):
    spec = models.CharField(max_length=70, verbose_name="Executable to open")

