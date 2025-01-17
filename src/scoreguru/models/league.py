from django.db import models
from django.utils.translation import gettext_lazy as _

class League(models.Model):
    name = models.CharField(max_length=100, help_text=_("League name, for example 'World Championship' or 'NHL'."))
    sport = models.CharField(max_length=50, help_text=_("Type of sport, e.g., 'Hockey', 'Soccer'."))
    description = models.TextField(blank=True, null=True, help_text=_("Optional description of the league."))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("League")
        verbose_name_plural = _("Leagues")
