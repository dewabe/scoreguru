from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scoreguru.models import Scoreboard

@admin.register(Scoreboard)
class ScoreboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'season', 'correct_home_goals', 'correct_visitor_goals', 'correct_winner', 'correct_tie', 'total_points')
    search_fields = ('user__username', 'season__name', 'season__league__name')
    list_filter = ('season__league', 'season', 'total_points')
    ordering = ('-total_points', 'season__name')

    fieldsets = (
        (None, {
            'fields': ('user', 'season'),
            'description': _('User and season details')
        }),
        (_('Correct Predictions'), {
            'fields': ('correct_home_goals', 'correct_visitor_goals', 'correct_winner', 'correct_tie'),
            'description': _('Details of correct predictions in the season')
        }),
        (_('Total Points'), {
            'fields': ('total_points',),
            'description': _('Total points earned during the season')
        })
    )

    def get_queryset(self, request):
        """Optimize queries by selecting related fields for efficiency."""
        return super().get_queryset(request).select_related('user', 'season', 'season__league')
