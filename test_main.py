import pytest
from main import StringCalculator


@pytest.fixture
def string_calculator():
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    return StringCalculator()


@pytest.mark.parametrize("str,expected", [
    (None, 0),
    (90, 0),
    ([], 0),
])
def test_add_invalid_params(string_calculator, str, expected):
    """
        Checks the validity of the opperands to see if an error is raised
    """
    with pytest.raises(ValueError, match="The operands have to be numbers separate by comma."):
        string_calculator.Add(str)


@pytest.mark.parametrize("str,expected", [
    ("", 0),
])
def test_add_empty_strings(string_calculator, str, expected):
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    assert string_calculator.Add(
        str) == expected, f'Adding {str} should give {expected} as a result.'


@pytest.mark.parametrize("str,expected", [
    ("1", 1),
    ("2", 2),
    ("20", 20),
    ("50", 50),
    ("100", 100),
    ("100000000", 100000000),
])
def test_add_one_string(string_calculator, str, expected):
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    total = string_calculator.Add(str)
    assert isinstance(total, int)
    assert total == expected
