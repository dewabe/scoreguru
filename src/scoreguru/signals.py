from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from django.utils.timezone import now
from scoreguru.models import Game, Prediction, Scoreboard

@receiver(post_save, sender=Game)
def update_predictions_and_scoreboard(sender, instance, **kwargs):
    """
    Update the predicted points and the scoreboard when the game results are saved.
    """
    if instance.home_goals is not None and instance.visitor_goals is not None:
        update_predictions(instance)
        update_scoreboard(instance.season)


def update_predictions(game):
    """
    Update all prediction points for the specified game.
    """
    predictions = Prediction.objects.filter(game=game)

    for prediction in predictions:
        # Check if home team goals or visitor team goals are correct
        prediction.correct_home_goals = 1 if prediction.predicted_home_goals == game.home_goals else 0
        prediction.correct_visitor_goals = 1 if prediction.predicted_visitor_goals == game.visitor_goals else 0

        # Determine the actual winner (home, visitor, or draw)
        actual_winner = (
            "home" if game.home_goals > game.visitor_goals else
            "visitor" if game.visitor_goals > game.home_goals else "draw"
        )

        # Determine the predicted winner (home, visitor, or draw)
        predicted_winner = (
            "home" if prediction.predicted_home_goals > prediction.predicted_visitor_goals else
            "visitor" if prediction.predicted_visitor_goals > prediction.predicted_home_goals else "draw"
        )

        # Check if the predicted winner is correct
        prediction.correct_winner = 1 if actual_winner == predicted_winner else 0

        # Check if the player predicted a draw correctly along with the exact goals
        prediction.correct_tie = 1 if actual_winner == "draw" and prediction.correct_home_goals and prediction.correct_visitor_goals else 0

        # Calculate the total points
        prediction.total_points = (
            prediction.correct_home_goals +
            prediction.correct_visitor_goals +
            prediction.correct_winner +
            prediction.correct_tie
        )

    # Bulk update the predictions with the new values
    Prediction.objects.bulk_update(predictions, ['correct_home_goals', 'correct_visitor_goals', 'correct_winner', 'correct_tie', 'total_points'])


def update_scoreboard(season):
    """
    Update the scoreboard based on the players' predictions for the season.
    """
    aggregated_scores = (
        Prediction.objects.filter(game__season=season)
        .values('user_id')
        .annotate(
            total_correct_home_goals=Sum('correct_home_goals'),
            total_correct_visitor_goals=Sum('correct_visitor_goals'),
            total_correct_winner=Sum('correct_winner'),
            total_correct_tie=Sum('correct_tie'),
            total_points=Sum('total_points')
        )
    )

    for score in aggregated_scores:
        Scoreboard.objects.update_or_create(
            user_id=score['user_id'],
            season=season,
            defaults={
                'correct_home_goals': score['total_correct_home_goals'],
                'correct_visitor_goals': score['total_correct_visitor_goals'],
                'correct_winner': score['total_correct_winner'],
                'correct_tie': score['total_correct_tie'],
                'total_points': score['total_points']
            }
        )
