from fizzbuzz import fizzbuzz
import pytest


def test_number_1():
    assert fizzbuzz(1) == "1"


def test_number_2():
    assert fizzbuzz(2) == "2"


def test_number_3():
    assert fizzbuzz(3) == "Fizz"


def test_number_4():
    assert fizzbuzz(4) == "4"


def test_number_5():
    assert fizzbuzz(5) == "Buzz"


def test_number_9():
    assert fizzbuzz(9) == "Fizz"


def test_number_8_is_not_fizz_or_buzz():
    assert not fizzbuzz(8) == "Buzz"


def test_number_10():
    assert fizzbuzz(10) == "Buzz"


def test_number_15():
    assert fizzbuzz(15) == "FizzBuzz"


@pytest.mark.parametrize("test_input,expected", [(1, "1"), (2, "2"), (4, "4")])
def test_regular_numbers(test_input, expected):
    assert fizzbuzz(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(3, "Fizz"), (6, "Fizz"), (9, "Fizz"), (12, "Fizz")]
)
def test_multiple_of_three(test_input, expected):
    assert fizzbuzz(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(5, "Buzz"), (10, "Buzz"), (15, "FizzBuzz")]
)
def test_multiple_of_five(test_input, expected):
    assert fizzbuzz(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(15, "FizzBuzz"), (30, "FizzBuzz"), (45, "FizzBuzz")]
)
def test_multiple_of_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected