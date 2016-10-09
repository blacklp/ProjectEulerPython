length = 1000000
cache = []

def init_cache():
    global cache
    cache = [-1] * length
    cache[1] = 1

def main():
    cache = init_cache()
    result = get_longest_collatz_seq(length)
    print result


def get_longest_collatz_seq(limit):
    max_length = 0
    result = 0
    for i in xrange(2, limit):
        seq_length = get_seq_length(i)
        if seq_length > max_length:
            max_length = seq_length
            result = i
    return result



def get_seq_length(start):
    global cache
    curr = start
    partial_len = 1 # counting the last one, i.e. 1
    while curr != 1 and curr >= start: # curr >= start means 'not yet seen'
        if curr % 2 == 0:
            curr = int(curr / 2)
        else:
            curr = 3*curr + 1
        partial_len += 1
    cache[start] = partial_len + cache[curr]
    # start != curr, curr unchanged
    return cache[start]


if __name__ == '__main__':
    main()
