from django.db import models
from django_extensions.db import fields as extension_fields

# Create your models here.
from turn_on.constants import CONNECTION_TYPE_CHOICES, INSTALLATION_TYPE_CHOICES


class Membership(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True, null=True)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)
    created_by = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, null=True, db_index=False,
                                   related_name='created_membership', blank=True)
    last_updated_by = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, null=True, db_index=False,
                                        related_name='updated_membership', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class TurnOn(models.Model):
    number = models.CharField(max_length=16, blank=True, null=True)
    first_name = models.CharField(max_length=24, blank=False, null=False)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    last_name = models.CharField(max_length=24, blank=False, null=False)
    spouse = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    cons = models.CharField(max_length=16, blank=True, null=True)
    install = models.CharField(max_length=64, choices=INSTALLATION_TYPE_CHOICES, blank=True, null=True, default='')
    connection = models.CharField(max_length=64, choices=CONNECTION_TYPE_CHOICES, default='')
    amount = models.DecimalField(max_digits=24, decimal_places=2, blank=True, null=True)
    or_number = models.CharField(max_length=64, blank=True, null=True)
    distance = models.IntegerField(blank=False, null=False)
    feeder = models.CharField(max_length=12, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)

    area = models.ForeignKey('locations.City', related_name='area_turn_on', null=True, on_delete=models.SET_NULL)
    municipality = models.ForeignKey('locations.City', related_name='municipality_turn_on', null=True,
                                     on_delete=models.SET_NULL)
    barangay = models.ForeignKey('locations.Barangay', related_name='barangay_turn_on', null=True,
                                 on_delete=models.SET_NULL)

    is_approved = models.BooleanField(default=False)

    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    or_created = models.ForeignKey('datesdim.DateDim', related_name='or_date', on_delete=models.SET_NULL, null=True,
                                   blank=True)
    approved_date = models.ForeignKey('datesdim.DateDim', related_name='date_approved', on_delete=models.SET_NULL,
                                      null=True, blank=True)
    membership = models.ForeignKey(Membership, related_name='membership_type', on_delete=models.SET_NULL, null=True,
                                   blank=True)

    created_by = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, null=True, db_index=False,
                                   related_name='created_turn_on', blank=True)
    last_updated_by = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, null=True, db_index=False,
                                        related_name='updated_turn_on', blank=True)

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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