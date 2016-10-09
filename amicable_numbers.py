def main():
    result = get_amicable_sum(10000)
    print result


def get_amicable_sum(limit):
    result = 0
    cache = init_cache(limit+1)

    for i in xrange(2, limit):
        divisor_sum = get_divisor_sum(i, cache)
        if is_amicable_pair(i, divisor_sum, cache):
            result += i
    return result


def init_cache(size):
    cache = [0] * size
    return cache


def get_divisor_sum(n, cache):
    if n >= len(cache):
        return -1 # it is not going to be amicable, since it is not in the range
    if cache[n] == 0:
        cache[n] = calculate_divisor_sum(n)
    return cache[n]


def calculate_divisor_sum(n):
    result = 1 # first divisor is always 1
    for i in xrange(2, int(n/2)+1):
        if n % i == 0:
            result += i
    return result


def is_amicable_pair(n, divisor_sum, cache):
    return divisor_sum != n and get_divisor_sum(divisor_sum, cache) == n


if __name__ == '__main__':
    main()
