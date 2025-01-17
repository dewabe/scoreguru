from django.db import models
from django.utils.translation import gettext_lazy as _

class Game(models.Model):
    season = models.ForeignKey(
        'Season',
        on_delete=models.CASCADE,
        help_text=_("The season this game belongs to.")
    )
    home_team = models.ForeignKey(
        'TeamsInSeason',
        related_name='home_games',
        on_delete=models.CASCADE,
        help_text=_("The home team participating in the game.")
    )
    visitor_team = models.ForeignKey(
        'TeamsInSeason',
        related_name='visitor_games',
        on_delete=models.CASCADE,
        help_text=_("The visitor team participating in the game.")
    )
    home_goals = models.PositiveIntegerField(
        blank=True, null=True,
        help_text=_("Goals scored by the home team (leave blank if the game has not been played yet).")
    )
    visitor_goals = models.PositiveIntegerField(
        blank=True, null=True,
        help_text=_("Goals scored by the visitor team (leave blank if the game has not been played yet).")
    )
    start_datetime = models.DateTimeField(
        help_text=_("The date and time when the game is scheduled to start.")
    )

    def __str__(self):
        return f"{self.home_team.team.name} vs {self.visitor_team.team.name} ({self.home_goals or '-'}-{self.visitor_goals or '-'})"

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")
        unique_together = ['season', 'home_team', 'visitor_team', 'start_datetime']
