def main():
    result = get_longest_collatz_seq(1000000)
    print result


def get_longest_collatz_seq(limit):
    max_length = 0
    result = 0
    for i in xrange(13, limit):
        seq_length = get_seq_length(i)
        if seq_length > max_length:
            max_length = seq_length
            result = i
    return result



def get_seq_length(start):
    curr = start
    result = 1 # counting the last one, i.e. 1
    while curr != 1:
        if curr % 2 == 0:
            curr /= 2
        else:
            curr = 3*curr + 1
        result+=1
    return result


if __name__ == '__main__':
    main()
