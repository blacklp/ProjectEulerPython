import math

# TODO: improve using http://en.wikipedia.org/wiki/Sieve_of_Atkin

def main():
    result = get_sum_of_primes_below(2000000)
    print result


def get_sum_of_primes_below(n):
    result = 0
    for i in xrange(2, n):
        if is_prime(i):
            result += i
    return result


def is_prime(n):
    for i in xrange(2, (int)(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
