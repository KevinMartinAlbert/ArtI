from django.test import TestCase
from django.db import connection
from ArtI.models import Creation, Creator


class SQLInjectionTestCase(TestCase):
    def setUp(self):
        self.creator = Creator.objects.create(name="Test Artist")

        self.test_obj = Creation.objects.create(
            title="Test Title",
            prompt="Test Prompt",
            description="Test Description",
            link="https://example.com",
            artist=self.creator,
        )

    def test_sql_injection_prevention(self):
        """
        Test that the application handles SQL injection attempts safely.
        """
        malicious_input = "'; DROP TABLE ArtI_Creation; --"

        try:
            response = Creation.objects.filter(title=malicious_input).exists()
        except Exception as e:
            self.fail(f"SQL Injection test failed due to an unexpected exception: {e}")

        self.assertFalse(
            response, "SQL Injection test failed: Malicious input caused issues."
        )

    def test_raw_query_sql_injection(self):
        """
        Ensure raw SQL queries using Django's cursor execute parameterized queries properly.
        """
        malicious_input = "'; DROP TABLE ArtI_Creation; --"
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT * FROM ArtI_creation WHERE title = %s", [malicious_input]
                )
                rows = cursor.fetchall()
            except Exception as e:
                self.fail(f"SQL Injection prevention failed: {e}")

        self.assertEqual(
            len(rows), 0, "SQL Injection test failed: Malicious input returned data."
        )
