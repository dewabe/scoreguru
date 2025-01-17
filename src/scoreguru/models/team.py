from django.db import models
from django.utils.translation import gettext_lazy as _

class Team(models.Model):
    name = models.CharField(max_length=100, help_text=_("Team name, for example 'Finland' or 'Canada'."))
    abbreviation = models.CharField(max_length=3, help_text=_("Three-letter abbreviation for the team, for example 'FIN' or 'CAN'."))
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True, help_text=_("Team logo image."))
    country_iso = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        help_text=_("Two-letter ISO Alpha-2 country code, for example 'FI' for Finland. Leave blank for non-national teams.")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
