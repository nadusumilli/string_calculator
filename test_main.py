import pytest
from main import StringCalculator


@pytest.fixture
def string_calculator():
    """Creates a fresh instance of the String Calculator before each test."""
    return StringCalculator()


@pytest.mark.parametrize("str,expected", [
    (None, 0),
    ("", 0),
])
def test_add_empty_strings(string_calculator, str, expected):
    assert string_calculator.Add(
        str) == expected, f'Adding {str} should give {expected} as a result.'
