def main():
    f = open('input_large_sum.txt', 'r')
    result = 0
    for line in f:
        result += long(line)
    print str(result)[0:10]

if __name__ == '__main__':
    main()
