from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
  create_at = models.DateTimeField(auto_now=True, verbose_name=_("Created at"))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

  user_fk = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.PROTECT, related_name="user_base")
