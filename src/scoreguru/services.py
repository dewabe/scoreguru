from .models import Scoreboard

def get_scoreboard_for_season(season_id):
    """
    Returns a scoreboard for a specific season, ordered by total_points in descending order.
    
    Args:
        season_id (int): The ID of the season for which the scoreboard is retrieved.
    
    Returns:
        QuerySet: Scoreboard entries for the given season, ordered by total_points.
    """
    return Scoreboard.objects.filter(season_id=season_id).order_by('-total_points')
