from django import apps
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models

from accounts.constants import USER, SUPERADMIN


class BaseProfileQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)


class BaseProfileManager(BaseUserManager):
  def get_queryset(self):
    return BaseProfileQuerySet(self.model, using=self._db)

  def actives(self):
    return self.get_queryset().actives()

  def create_user(self, email, username=None, password=None, user_type=USER):
    email_validator = EmailValidator()
    try:
      email_validator(email)
      if not username:
        username = 'NoUsername'
      user = self.model(
        username=username,
        email=self.normalize_email(email),
        user_type=user_type
      )

      user.set_password(password)
      user.save(using=self._db)
      return user
    except ValidationError:
      return False

  def create_superuser(self, email, password, username=None):
    user = self.create_user(
      username=username,
      email=email,
      password=password,
    )
    user.user_type = SUPERADMIN
    user.is_admin = True
    user.save(using=self._db)
    return user