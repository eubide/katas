# A leap year is defined as one that is divisible by 4,
# but is not otherwise divisible by 100 unless it is also divisible by 400.


def is_leap_year(number):
    if not number % 4 and (number % 100 or not number % 400):
        return True
    else:
        return False
