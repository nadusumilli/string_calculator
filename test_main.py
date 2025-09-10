import pytest
from main import StringCalculator


@pytest.fixture
def string_calculator():
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    return StringCalculator()


@pytest.mark.parametrize("str", [
    None,
    90,
    [],
])
def test_add_invalid_type(string_calculator, str):
    """
        Checks the validity of the opperands to see if an error is raised
    """
    with pytest.raises(ValueError, match="The operands have to be numbers separate by comma."):
        string_calculator.Add(str)


@pytest.mark.parametrize("str", [
    "hello",
    "why",
    "2.00",
    "['hello']",
    "55.44",
    "ehy",
])
def test_add_invalid_string(string_calculator, str):
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    with pytest.raises(ValueError, match="The value of the operands have to be numbers."):
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
