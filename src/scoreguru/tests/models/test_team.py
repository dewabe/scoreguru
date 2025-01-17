from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from scoreguru.models import Team

class TeamModelTest(TestCase):
    def setUp(self):
        # Create temporary image for testing the logo field
        self.logo_file = SimpleUploadedFile(
            "test_logo.png",
            content=b"fake_image_content",
            content_type="image/png"
        )

    def test_create_team_with_minimal_data(self):
        """Test that a team can be created with only a name and abbreviation."""
        team = Team.objects.create(
            name="Finland",
            abbreviation="FIN"
        )
        self.assertEqual(team.name, "Finland")
        self.assertEqual(team.abbreviation, "FIN")
        self.assertFalse(team.logo)

    def test_create_team_with_logo(self):
        """Test that a team can be created with a logo."""
        team = Team.objects.create(
            name="Canada",
            abbreviation="CAN",
            logo=self.logo_file
        )
        self.assertEqual(team.name, "Canada")
        self.assertEqual(team.abbreviation, "CAN")
        self.assertIsNotNone(team.logo)

    def test_str_representation(self):
        """Test that the string representation of a team is its name."""
        team = Team.objects.create(name="Sweden", abbreviation="SWE")
        self.assertEqual(str(team), "Sweden")

    def tearDown(self):
        # Close any temporary files after tests
        self.logo_file.close()
