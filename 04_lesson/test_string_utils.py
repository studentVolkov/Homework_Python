import pytest

from string_utils import StringUtils

string_util = StringUtils()


# Test Case 1: Тестирование функциональности "capitalize"
@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    ("sergei", "Sergei"),
    ("sergei", "Sergei"),
    ("volk sergei", "Volk sergei"),
    ("ser^gei", "Ser^gei"),
    ("sergei1", "Sergei1"),

    # Негативные проверки:
    ("", ""),
    ("Sergei", "Sergei"),
    ("ABC", "Abc"),
    ("123abc", "123abc")
])
def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result


# Test Case 2: Тестирование функциональности "trim"
@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    (" abc", "abc"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),
    # Негативные проверки:
    ("", ""),
    ("vol", "vol"),
    ("123  ", "123  ")
])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result


# Test Case 4: Тестирование функциональности "contains"
@pytest.mark.parametrize('string, symbol, result', [
    #  Позитивные проверки:
    ("sergei", "s", True),
    (" test", "t", True),
    ("Sergei-who", "-", True),
    ("123", "1", True),
    ("ABC", "C", True),
    ("", "", True),
    # Негативные проверки:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),
    ("hello", "!", False),
    ("", "x", False),
    ("hello", "xyz", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 5: Тестирование функциональности "delete_symbol"


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("sergei", "i", "serge"),
    ("Volk", "o", "Vlk"),
    ("Town", "T", "own"),
    ("123", "1", "23"),
    ("Sergei-Who", "-", "SergeiWho"),

    # Негативные проверки:
    ("Volkov", "W", "Volkov"),
    ("", "", ""),
    ("", "S", ""),
    ("book", "", "book")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result
