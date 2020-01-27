from django import forms

from turn_on.models import Membership, TurnOn


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('name', 'active')


class TurnOnForm(forms.ModelForm):
    class Meta:
        model = TurnOn
        fields = (
            'number',
            'first_name',
            'middle_name',
            'last_name',
            'spouse',
            'address',
            'cons',
            'install',
            'connection',
            'amount',
            'or_number',
            'distance',
            'feeder',
            'year',
            'area',
            'municipality',
            'barangay',
            'membership'
        )