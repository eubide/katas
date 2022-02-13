# Read Me

## Description

Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Sample output:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
... etc up to 100
```

## Notes

**Coverage**

```
pytest --cov=fizzbuzz

pytest --cov=fizzbuzz --cov-report=term-missing --cov-branch
```

**References**

https://www.cyber-dojo.org/creator/choose_problem

https://docs.pytest.org/en/6.2.x/parametrize.html
