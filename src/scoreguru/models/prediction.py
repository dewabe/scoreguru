from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("The user who made the prediction.")
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        help_text=_("The game being predicted.")
    )
    predicted_home_goals = models.PositiveIntegerField(
        help_text=_("Predicted goals for the home team.")
    )
    predicted_visitor_goals = models.PositiveIntegerField(
        help_text=_("Predicted goals for the visitor team.")
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
        return f"Prediction by {self.user.username} for {self.game}"

    class Meta:
        verbose_name = _("Prediction")
        verbose_name_plural = _("Predictions")
        unique_together = ['user', 'game']
