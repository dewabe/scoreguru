from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scoreguru.models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'logo', 'country_iso')
    search_fields = ('name', 'abbreviation')
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'abbreviation', 'logo', 'country_iso'),
            'description': _('Team information')
        }),
    )

    def get_queryset(self, request):
        """Optimize queries to include relevant fields."""
        return super().get_queryset(request)
