# test_teams_in_season.py

from django.test import TestCase
from django.db import IntegrityError
from scoreguru.models import Team, Season, TeamsInSeason, League

class SeasonModelTest(TestCase):
    def setUp(self):
        # Create a league instance for the season
        self.league = League.objects.create(
            name="World Championship",
            sport="Hockey",
            description="The official ice hockey world championship organized annually."
        )
        # Create a season instance for testing
        self.season = Season.objects.create(
            league=self.league,
            name="2025 World Championship",
            start_date="2025-05-01",
            end_date="2025-05-31"
        )

    def test_create_season(self):
        """Test that a season can be created successfully."""
        self.assertEqual(self.season.name, "2025 World Championship")
        self.assertEqual(self.season.start_date, "2025-05-01")
        self.assertEqual(self.season.end_date, "2025-05-31")
        self.assertEqual(self.season.league.name, "World Championship")

    def test_str_representation(self):
        """Test the string representation of a season object."""
        self.assertEqual(str(self.season), "World Championship - 2025 World Championship")

    def tearDown(self):
        # Clean up created objects
        self.season.delete()
        self.league.delete()


class TeamsInSeasonModelTest(TestCase):
    def setUp(self):
        # Create a team and a season for testing
        self.team = Team.objects.create(name="Finland", abbreviation="FIN")
        self.league = League.objects.create(
            name="World Championship",
            sport="Hockey",
            description="The official ice hockey world championship organized annually."
        )
        self.season = Season.objects.create(
            league=self.league,
            name="2025 World Championship",
            start_date="2025-05-01",
            end_date="2025-05-31"
        )

    def test_create_teams_in_season(self):
        """Test that a team can be correctly linked to a season."""
        teams_in_season = TeamsInSeason.objects.create(team=self.team, season=self.season)
        self.assertEqual(teams_in_season.team.name, "Finland")
        self.assertEqual(teams_in_season.season.name, "2025 World Championship")

    def test_str_representation(self):
        """Test the string representation of a TeamsInSeason object."""
        teams_in_season = TeamsInSeason.objects.create(team=self.team, season=self.season)
        self.assertEqual(str(teams_in_season), "Finland in 2025 World Championship")

    def tearDown(self):
        # Clean up created objects after each test
        self.team.delete()
        self.season.delete()
