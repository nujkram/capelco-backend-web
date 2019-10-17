from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import Account


class UserCreationForm(forms.ModelForm):
  email = forms.EmailField()
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

  class Meta:
    model = Account
    fields = ('email', 'username', 'password')

  def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError("Password don't match")
    return password2

  def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user


class UserChangeForm(forms.ModelForm):
  """A form for updating users. Includes all the fields on
  the user, but replaces the password field with admin's
  password hash display field.
  """
  # password = ReadOnlyPasswordHashField()
  password = ReadOnlyPasswordHashField(label=("Password"),
                                       help_text=("Raw passwords are not stored, so there is no way to see "
                                                  "this user's password, but you can change the password "
                                                  "using <a href=\"../password/\">this form</a>."))

  class Meta:
    model = Account
    fields = ('email', 'password', 'is_active', 'is_admin')

  def clean_password(self):
    # Regardless of what the user provides, return the initial value.
    # This is done here, rather than on the field, because the
    # field does not have access to the initial value
    return self.initial["password"]


class UserAdmin(BaseUserAdmin):
  # The forms to add and change user instances
  form = UserChangeForm
  add_form = UserCreationForm

  list_display = ('email', 'user_type', 'created')
  list_filter = ('user_type',)
  search_fields = ('email',)
  ordering = ('-created',)
  filter_horizontal = ()

  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Permissions', {'fields': ('is_admin', 'user_type')})
  )

  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'username', 'password1', 'password2')}
     ),
  )

admin.site.register(Account, UserAdmin)

admin.site.unregister(Group)