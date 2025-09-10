import pytest
from main import StringCalculator


@pytest.fixture
def string_calculator():
    """Creates a fresh instance of the String Calculator before each test."""
    return StringCalculator()


def test_add_strings(string_calculator):
    assert string_calculator.Add
