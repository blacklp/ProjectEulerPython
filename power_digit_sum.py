import math

def main():
    result = get_sum_of_digits(2, 1000)
    print result


def get_sum_of_digits(base, power):
    n = int(math.pow(base, power))
    result = 0
    while n > 0:
        digit = int(n % 10)
        result += digit
        n = int(n/10)
    return result


if __name__ == '__main__':
    main()
