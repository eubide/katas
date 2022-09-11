def Fibonacci(i: int):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return Fibonacci(i - 1) + Fibonacci(i - 2)
    else:
        return -1
