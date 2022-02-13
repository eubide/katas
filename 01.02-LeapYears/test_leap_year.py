from leap_year import is_leap_year
# import pytest

# https://scienceworld.wolfram.com/astronomy/LeapYear.html
# The complete list of leap years in the first half of the 21st century
# is therefore 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028,
# 2032, 2036, 2040, 2044, and 2048.


def test_year_2000_is_leap():
    assert is_leap_year(2000) is True


def test_year_2001_is_common():
    assert is_leap_year(2001) is False


def test_year_2004_is_leap():
    assert is_leap_year(2004) is True


def test_year_2008_is_leap():
    assert is_leap_year(2008) is True


def test_year_2010_is_common():
    assert is_leap_year(2010) is False


def test_year_1996_is_leap():
    assert is_leap_year(1996) is True


# def test_year_1900_is_common():
#    assert is_leap_year(1996) is False


def test_year_2010_is_common():
    assert is_leap_year(2010) is False
