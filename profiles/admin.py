from django.contrib import admin

# Register your models here.
from profiles.models import BaseProfile, Gender


class BaseProfileAdmin(admin.ModelAdmin):
  list_display = ('created', 'account', 'first_name', 'last_name')
  list_filter = ('gender',)
  search_fields = ('first_name', 'last_name', 'user')
  ordering = ('-created',)


admin.site.register(BaseProfile, BaseProfileAdmin)


class GenderAdmin(admin.ModelAdmin):
  list_display = ('name',)


admin.site.register(Gender, GenderAdmin)
