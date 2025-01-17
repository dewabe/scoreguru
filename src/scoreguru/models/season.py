from django.db import models
from django.utils.translation import gettext_lazy as _

class Season(models.Model):
    league = models.ForeignKey(
        'League',
        on_delete=models.CASCADE,
        help_text=_("The league to which this season belongs.")
    )
    name = models.CharField(
        max_length=100,
        help_text=_("Season name, for example '2025 World Championship'.")
    )
    start_date = models.DateField(help_text=_("Start date of the season."))
    end_date = models.DateField(help_text=_("End date of the season."))
    visible = models.BooleanField(
        default=True,
        help_text=_("Indicates whether the season is visible in the UI.")
    )

    def __str__(self):
        return f"{self.league.name} - {self.name}"

    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")


class TeamsInSeason(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, help_text=_("The team participating in the season."))
    season = models.ForeignKey('Season', on_delete=models.CASCADE, help_text=_("The season in which the team is participating."))

    def __str__(self):
        return f"{self.team.name} in {self.season}"

    class Meta:
        verbose_name = _("Team in Season")
        verbose_name_plural = _("Teams in Season")
        constraints = [
            models.UniqueConstraint(fields=['team', 'season'], name='unique_team_in_season')
        ]