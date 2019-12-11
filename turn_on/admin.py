from django.contrib import admin

# Register your models here.
from turn_on.models import Membership, TurnOn


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TurnOnAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'first_name',
        'last_name',
        'connection',
        'created',
    )
    list_filter = ('connection',)

    search_fields = ('first_name', 'last_name', 'municipality',)


admin.site.register(Membership, MembershipAdmin)
admin.site.register(TurnOn, TurnOnAdmin)