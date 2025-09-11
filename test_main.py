import pytest
from main import StringCalculator
from main import NegativeNumberException, InvalidValueException


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
    with pytest.raises(InvalidValueException, match="The operands have to be numbers separate by comma."):
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
    with pytest.raises(InvalidValueException, match="The value of the operands have to be numbers."):
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
    ("50", 50),
    ("100", 100),
    ("234", 234),
])
def test_add_one_number_string(string_calculator, str, expected):
    """
        Test case to see if the single integer is returned.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("1,1", 2),
    ("2,4", 6),
    ("2,9", 11),
    ("50,5", 55),
    ("100,2", 102),
    ("123,25", 148),
    ("1,1", 2),
    ("1,10", 11),
    ("5,10", 15),
    ("5,7", 12),
    ("5,20", 25),
])
def test_add_two_number_string(string_calculator, str, expected):
    """
        Test case for two values separated by comma.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("1,1,1", 3),
    ("2,4,5", 11),
    ("2,9,1", 12),
    ("50,5,6,3,7,5,8", 84),
    ("15,2,1,2,10", 30),
    ("10,25", 35),
    ("1,1,567", 569),
    ("1,10,100", 111),
])
def test_add_dynamic_number_string(string_calculator, str, expected):
    """
        Test case for unknown number of values separated by comma.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("1.0,1.0", 2.0),
    ("2.0,4.0", 6.0),
    ("2.0,9.0", 11.0),
    ("50.00,5.0", 55.0),
])
def test_add_float_string(string_calculator, str, expected):
    """
        Test case to check float values.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("1\n1", 2),
    ("2\n4", 6),
    ("2\n9", 11),
    ("5\n10", 15),
    ("5\n7", 12),
    ("5\n20", 25),
])
def test_add_newline_string(string_calculator, str, expected):
    """
        Test case for newline custom delimeter.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("//[*]\n1*1", 2),
    ("//[,]\n2,4", 6),
    ("//[|]\n2|9", 11),
    ("//[,]\n5,10", 15),
    ("//[|]\n5|7", 12),
    ("//[*]\n5*20", 25),
])
def test_add_custom_delimeter_string(string_calculator, str, expected):
    """
        Test case for checking custom delimeter.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("//[*]\n-1*1", "-1"),
    ("//[,]\n2,-4", "-4"),
    ("//[|]\n-2|9", "-2"),
])
def test_add_negative_string(string_calculator, str, expected):
    """
        Testing for single negative number.
    """
    with pytest.raises(NegativeNumberException, match=f"negatives not allowed: {expected}"):
        string_calculator.Add(str)


@pytest.mark.parametrize("str,expected", [
    ("//[*]\n-1*-1*-10", "-1,-1,-10"),
    ("//[,]\n-2,-4,-40", "-2,-4,-40"),
    ("//[|]\n-2|-9|-90", "-2,-9,-90"),
])
def test_add_multiple_negative_string(string_calculator, str, expected):
    """
        Testing for multiple negative numbers.
    """
    with pytest.raises(NegativeNumberException, match=f"negatives not allowed: {expected}"):
        string_calculator.Add(str)


def test_get_called_count(string_calculator):
    """
        Test functionality to check the count of the add functionality.
    """
    count = 0
    string_calculator.Add("2,4")
    count += 1
    assert string_calculator.GetCalledCount() == count
    string_calculator.Add("2,4")
    count += 1
    assert string_calculator.GetCalledCount() == count
    string_calculator.Add("2,4")
    count += 1
    assert string_calculator.GetCalledCount() == count
    string_calculator.Add("2,4")
    count += 1
    assert string_calculator.GetCalledCount() == count


@pytest.mark.parametrize("str,expected", [
    ("//[*]\n1*1001", 1),
    ("//[,]\n2,4444", 2),
    ("//[|]\n2|9999", 2),
])
def test_ignore_greater_than_1000_string(string_calculator, str, expected):
    """
        Test functionality to check that numbers greater than 1000 are removed from the sum.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("//[**]\n1**1001", 1),
    ("//[,,]\n2,,4444", 2),
    ("//[||]\n2||9999", 2),
])
def test_add_multi_string_delimeter(string_calculator, str, expected):
    """
        Test functionality to check for multi delimeter splitting.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("//[*][|]\n1*1001|24", 25),
    ("//[,][$]\n2,4444$20", 22),
    ("//[|][)]\n2|9999)60", 62),
])
def test_add_multi_delimeter_string(string_calculator, str, expected):
    """
        Test functionality to check for multi delimeter splitting.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'


@pytest.mark.parametrize("str,expected", [
    ("//[**][||]\n1**1001||24", 25),
    ("//[,,][\\]\n2,,4444\\20", 22),
    ("//[||][()]\n2||9999()60", 62),
])
def test_add_multi_delimeter_multi_string(string_calculator, str, expected):
    """
        Test functionality to check for multi delimeter splitting.
    """
    total = string_calculator.Add(str)
    assert isinstance(
        total, (int, float)), f'Return value of the Add function should be integer or float'
    assert total == expected, f'Total value for {str} should be {expected} but got {total}'
