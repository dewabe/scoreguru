from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scoreguru.models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'predicted_home_goals', 'predicted_visitor_goals')
    search_fields = ('user__username', 'game__season__name', 'game__home_team__team__name', 'game__visitor_team__team__name')
    list_filter = ('game__season__league', 'game__season')
    ordering = ('game__start_datetime',)

    fieldsets = (
        (None, {
            'fields': ('user', 'game', 'predicted_home_goals', 'predicted_visitor_goals'),
            'description': _('Prediction details')
        }),
    )

    def get_queryset(self, request):
        """Optimize queries by selecting related fields for efficiency."""
        return super().get_queryset(request).select_related('user', 'game__season', 'game__home_team__team', 'game__visitor_team__team', 'game__season__league')
