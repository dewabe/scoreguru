from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Scoreboard(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("The user whose score is being tracked.")
    )
    season = models.ForeignKey(
        'Season',
        on_delete=models.CASCADE,
        help_text=_("The season for which the scoreboard entry is valid.")
    )
    correct_home_goals = models.PositiveIntegerField(
        default=0,
        help_text=_("Correct predictions for home team goals.")
    )
    correct_visitor_goals = models.PositiveIntegerField(
        default=0,
        help_text=_("Correct predictions for visitor team goals.")
    )
    correct_winner = models.PositiveIntegerField(
        default=0,
        help_text=_("Correct predictions for the winner.")
    )
    correct_tie = models.PositiveIntegerField(
        default=0,
        help_text=_("Correct predictions for ties.")
    )
    total_points = models.PositiveIntegerField(
        default=0,
        help_text=_("The total points earned by the user in this season.")
    )

    def __str__(self):
        return f"{self.user.username} - {self.season.name}: {self.total_points} points"

    class Meta:
        verbose_name = _("Scoreboard")
        verbose_name_plural = _("Scoreboards")
        unique_together = ['user', 'season']
        
