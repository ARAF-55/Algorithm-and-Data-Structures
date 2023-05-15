# factorial anb fibonacci

def factorial(n):
    assert 0 <= n == int(n), 'The value is out of constraints'
    if n == 1 or 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    assert 0 <= n == int(n), 'The value is out of constraints'
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(digit):
    assert 0 <= digit == int(digit), 'The value is out of constraints'
    kala = str(digit)
    if len(kala) == 1:
        return int(kala[0])
    return int(kala[0]) + sum_of_digits(int(kala[1:]))


def sum_of_digits_num(digit):
    assert 0 <= digit == int(digit), 'The value is out of constraints'
    if int(digit % 10) == digit:
        return digit
    return int(digit % 10) + sum_of_digits_num(int(digit / 10))


def power_of_number(x, n):
    assert 0 <= x == int(x), 'The value is out of constraints'
    assert 0 <= n == int(n), 'The value is out of constraints'
    if n == 1:
        return x
    return x * power_of_number(x, n - 1)


def gcd(x, y):
    assert 0 < x == int(x), 'The value is out of constraints'
    assert 0 < y == int(y), 'The value is out of constraints'
    assert x > y, 'please put the greater value at first, then the lesser value'
    if x % y == 0:
        return y
    return gcd(y, x % y)


def decimal_to_binary(digit):
    assert 0 <= digit == int(digit), 'The value must be an integer'
    if digit == 0:
        return digit
    return digit % 2 + 10 * decimal_to_binary(int(digit/2))


print(factorial(7))
print(fibonacci(7))
print(sum_of_digits(18293))
print(sum_of_digits_num(18293))
print(power_of_number(5, 3))
print(gcd(48, 18))
print(decimal_to_binary(13))
