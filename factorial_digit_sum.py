def main():
    result = factorial_digit_sum(100)
    print result


def factorial_digit_sum(n):
    factorial = calculate_factorial(n)
    return get_digit_sum(factorial)


def calculate_factorial(n):
    result = 1
    for i in xrange(1, n+1):
        result *= i
    return result
        

def get_digit_sum(n):
    result = 0
    while n > 0:
        digit = n % 10
        result += digit
        n /= 10
    return result


if __name__ == '__main__':
    main()
