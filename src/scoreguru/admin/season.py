from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scoreguru.models import Season, TeamsInSeason

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'start_date', 'end_date', 'visible')
    search_fields = ('name', 'league__name')
    list_filter = ('league', 'start_date')
    ordering = ('start_date', 'name')

    fieldsets = (
        (None, {
            'fields': ('league', 'name', 'start_date', 'end_date', 'visible'),
            'description': _('Details of the season')
        }),
    )


@admin.register(TeamsInSeason)
class TeamsInSeasonAdmin(admin.ModelAdmin):
    list_display = ('team', 'season')
    search_fields = ('team__name', 'season__name')
    list_filter = ('season__league', 'season')
    ordering = ('season', 'team')

    def get_queryset(self, request):
        """Optimize queries by selecting related fields for efficiency."""
        return super().get_queryset(request).select_related('team', 'season', 'season__league')
