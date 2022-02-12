from fizzbuzz import fizzbuzz


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
