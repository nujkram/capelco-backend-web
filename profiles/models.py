from django.db import models
from django_extensions.db import fields as extension_fields

# Create your models here.
from profiles.managers import BaseProfileManager


class Gender(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class BaseProfile(models.Model):
    first_name = models.CharField(max_length=32, blank=True, null=True, default='')
    middle_name = models.CharField(max_length=32, blank=True, null=True, default='')
    last_name = models.CharField(max_length=32, blank=True, null=True, default='')

    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    gender = models.ForeignKey(Gender, related_name='gender_profiles', on_delete=models.SET_NULL, null=True, blank=True)
    account = models.OneToOneField(
        'accounts.Account',
        on_delete=models.CASCADE
    )

    objects = BaseProfileManager()

    class Meta:
        ordering = ('account', '-created')

    def __str__(self):
        return self.get_full_name()

    def get_casual_name(self):
        if self.first_name != '':
            return self.first_name
        return 'Unnamed'

    def get_name(self):
        if self.first_name != '' and self.last_name != '':
            return '{} {}'.format(
                self.first_name, self.last_name
            )
        else:
            if self.account.username is not None:
                return self.account.username
            return self.account.email

    def get_full_name(self):
        if self.first_name != '' and self.last_name != '' and self.middle_name != '':
            return '{}, {} {}.'.format(
                self.last_name, self.first_name, self.middle_name[0]
            )
        elif self.first_name != '' and self.last_name != '':
            return '{}, {}'.format(
                self.last_name, self.first_name
            )
        else:
            try:
                if self.account.username is not None:
                    return self.account.username
            except AttributeError:
                return 'Unnamed'
            return 'Unnamed'
