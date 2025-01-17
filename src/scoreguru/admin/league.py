from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scoreguru.models import League

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'description')
    search_fields = ('name', 'sport')
    list_filter = ('sport',)
    ordering = ('name',)

    def get_queryset(self, request):
        """Optimize queries by selecting related fields if needed."""
        return super().get_queryset(request).select_related()

    fieldsets = (
        (None, {
            'fields': ('name', 'sport', 'description'),
            'description': _('Basic information about the league')
        }),
    )

    def __str__(self):
        return self.name
