import pytest
from django.core.management import call_command

@pytest.fixture
def test_polls(db) -> None:
    fixtures = ['initial_data.json']

    for fixture in fixtures:
        call_command('loaddata', fixture)
