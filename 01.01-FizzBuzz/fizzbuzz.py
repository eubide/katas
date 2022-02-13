def fizzbuzz(number):
    if not number % 15:
        return "FizzBuzz"
    elif not number % 3:
        return "Fizz"
    elif not number % 5:
        return "Buzz"
    else:
        return str(number)
