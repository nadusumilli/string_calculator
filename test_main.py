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
    "['hello']",
    "ehy",
])
def test_add_invalid_string(string_calculator, str):
    """
        Checks the validity of the string arguments of the function.
    """
    with pytest.raises(ValueError, match="The value of the operands have to be numbers."):
        string_calculator.Add(str)


@pytest.mark.parametrize("str,expected", [
    ("", 0),
])
def test_add_empty_strings(string_calculator, str, expected):
    """
        Testing to see if the empty string returns 0
    """
    assert string_calculator.Add(
        str) == expected, f'Adding {str} should give {expected} as a result.'


@pytest.mark.parametrize("str,expected", [
    ("1", 1),
    ("2", 2),
    ("20", 20),
    ("50.00", 50),
    ("-50.00", -50),
    ("-50", -50),
    ("100", 100),
    ("100000000", 100000000),
])
def test_add_one_string(string_calculator, str, expected):
    """
        Test case to see if the single integer is returned.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected}'


@pytest.mark.parametrize("str,expected", [
    ("1,1", 2),
    ("2,4", 6),
    ("2,9", 11),
    ("50,5", 55),
    ("100,2", 102),
    ("100000000,25", 100000025),
    ("-1,1", 0),
    ("-1,10", 9),
    ("-5,10", 5),
    ("-5,-7", -12),
    ("-5,-20", -25),
])
def test_add_two_string(string_calculator, str, expected):
    """
        Test case for two values separated by comma.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected}'


@pytest.mark.parametrize("str,expected", [
    ("1,1,1", 3),
    ("2,4,5", 11),
    ("2,9,-1", 10),
    ("50,5,6,3,7,5,8", 84),
    ("100,2,1,2,-100", 5),
    ("100000000,25,-999999", 99000026),
    ("-1,1,567", 567),
    ("-1,10,100", 109),
])
def test_add_dynamic_number_string(string_calculator, str, expected):
    """
        Test case for unknown number of values separated by comma.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected}'


@pytest.mark.parametrize("str,expected", [
    ("1,1", 2),
    ("2,4", 6),
    ("2,9", 11),
    ("50.00,5", 55),
    ("100,2", 102),
    ("100000000,25", 100000025),
    ("-1,1", 0),
    ("-1,10", 9),
    ("-5,10", 5),
    ("-5,-7", -12),
    ("-5,-20", -25),
])
def test_add_float_string(string_calculator, str, expected):
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected}'


@pytest.mark.parametrize("str,expected", [
    ("1\n1", 2),
    ("2\n4", 6),
    ("2\n9", 11),
    ("-5\n10", 5),
    ("-5\n-7", -12),
    ("-5\n-20", -25),
])
def test_add_newline_string(string_calculator, str, expected):
    """
        Creates a fresh instance of the String Calculator before each test.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected}'
