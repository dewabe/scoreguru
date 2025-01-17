from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scoreguru.models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('season', 'get_home_team_name', 'get_visitor_team_name', 'start_datetime', 'home_goals', 'visitor_goals')
    search_fields = ('season__name', 'home_team__team__name', 'visitor_team__team__name')
    list_filter = ('season__league', 'season', 'start_datetime')
    ordering = ('start_datetime',)

    fieldsets = (
        (None, {
            'fields': ('season', 'home_team', 'visitor_team', 'start_datetime'),
            'description': _('Details of the game')
        }),
        (_('Results'), {
            'fields': ('home_goals', 'visitor_goals'),
            'description': _('Final scores of the game (if available)')
        })
    )

    def get_home_team_name(self, obj):
        return obj.home_team.team.name
    
    def get_visitor_team_name(self, obj):
        return obj.visitor_team.team.name

    get_home_team_name.short_description = _("Home Team")
    get_visitor_team_name.short_description = _("Visitor Team")

    def get_queryset(self, request):
        """Optimize queries by selecting related fields for efficiency."""
        return super().get_queryset(request).select_related('season', 'home_team__team', 'visitor_team__team', 'season__league')
