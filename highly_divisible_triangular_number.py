import math

def erathostenes_sieve(n):
    arr = [True] * n # all n list positions contain True
    arr[0] = arr[1] = False
    
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if arr[i]:
            j = i*i
            while j < n:
                arr[j] = False
                j += i
    return [i for i in xrange(2, n) if arr[i]]

prime_list = erathostenes_sieve(100000)

def main():
    result = get_highly_divisible_triangle(500)
    print result


def get_highly_divisible_triangle(min_nb_divisors):
    i = 1
    n = -1
    while True:
        n = get_nth_number(i)
        if has_over_nb_divisors(n, min_nb_divisors):
            break
        i+=1
    return n


def get_nth_number(n):
    return n*(n+1)/2

def has_over_nb_divisors(n, nb_divs):
    result = 1
    remain = n
    for i in prime_list:
        if i * i > n:
            return result * 2 > nb_divs
        exponent = 1
        while remain % i == 0:
            exponent += 1
            remain /= i
        result *= exponent
        if remain == 1:
            return result > nb_divs
    return result > nb_divs


def is_prime(n):
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
