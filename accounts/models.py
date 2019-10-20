from django.apps import apps
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.constants import USERNAME_REGEX, USER_TYPE_CHOICES, USER
from accounts.managers import BaseProfileManager
from profiles.models import BaseProfile


class Account(AbstractBaseUser):
    username = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=USERNAME_REGEX,
                message='Username can only contain alphanumeric characters and the following characters: . -',
                code='Invalid Username'
            )
        ],
        unique=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default=USER, max_length=3)

    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    created_by = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.SET_NULL,
        related_name="account_creator",
        db_index=False
    )

    USERNAME_FIELD = 'email'

    objects = BaseProfileManager()

    class Meta:
        ordering = ('username', '-created',)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def base_profile(self):
        BaseProfile = apps.get_model('profiles.BaseProfile')
        try:
            return BaseProfile.objects.get(account=self)
        except BaseProfile.DoesNotExist:
            profile = BaseProfile.objects.create(account=self)
            return profile


@receiver(post_save, sender=Account)
def create_base_profile(sender, instance=None, created=False, **kwargs):
  if created:
    BaseProfile.objects.create(account=instance)
