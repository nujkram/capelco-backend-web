from django import forms

from turn_on.models import Membership, TurnOn


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('name',)


class TurnOnForm(forms.ModelForm):
    class Meta:
        model = TurnOn
        fields = '__all__'