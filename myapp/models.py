from django.db import models
from django.contrib.auth.models import User
import os

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.user.id, filename)


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    docfile = models.FileField(upload_to=get_upload_path)