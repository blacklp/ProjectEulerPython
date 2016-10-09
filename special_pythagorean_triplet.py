def main():
    result = find_pithagorean_triplet(1000)
    print result


def find_pithagorean_triplet(n):
    for a in xrange(n):
        for b in xrange(n):
            if a == b:
                break
            c = n - a - b
            if (a*a + b*b) == c*c:
                return a*b*c


if __name__ == '__main__':
    main()
