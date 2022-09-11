from tarfile import FIFOTYPE
from nth_fibonacci import Fibonacci


def test_Fibonacci_0():
    assert Fibonacci(0) == 0


def test_Fibonacci_1():
    assert Fibonacci(1) == 1


def test_Fibonacci_2():
    assert Fibonacci(2) == 1


def test_Fibonacci_3():
    assert Fibonacci(3) == 2


def test_Fibonacci_4():
    assert Fibonacci(4) == 3


def test_Fibonacci_5():
    assert Fibonacci(5) == 5


def test_Fibonacci_6():
    assert Fibonacci(6) == 8


def test_Fibonacci_7():
    assert Fibonacci(7) == 13


def test_Fibonacci_20():
    assert Fibonacci(20) == 6765


def test_Fibonacci_minus_1():
    assert Fibonacci(-1) == -1


def test_Fibonacci_minus_2():
    assert Fibonacci(-2) == -1
