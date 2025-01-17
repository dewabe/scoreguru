from django.test import TestCase
from scoreguru.models import League

class LeagueModelTest(TestCase):
    def setUp(self):
        # Create a league instance for testing
        self.league = League.objects.create(
            name="World Championship",
            sport="Hockey",
            description="The official ice hockey world championship organized annually."
        )

    def test_create_league(self):
        """Test that a league can be created successfully."""
        self.assertEqual(self.league.name, "World Championship")
        self.assertEqual(self.league.sport, "Hockey")
        self.assertEqual(self.league.description, "The official ice hockey world championship organized annually.")

    def test_str_representation(self):
        """Test the string representation of a league object."""
        self.assertEqual(str(self.league), "World Championship")

    def test_blank_description(self):
        """Test that the description can be blank or null."""
        blank_league = League.objects.create(name="Local League", sport="Soccer", description="")
        self.assertEqual(blank_league.description, "")

    def tearDown(self):
        # Clean up created league
        self.league.delete()
