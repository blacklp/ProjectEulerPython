def main():
    f = open('input__largest_product_in_a_series.txt', 'r')
    file_content = f.read().replace('\n', '')
    result = find_adjacent_digits_with_largest_product(file_content, 13)
    print result


def find_adjacent_digits_with_largest_product(file_content, num_digits):
    result = 0
    length = len(file_content)
    for i in xrange(0, length - num_digits):
        product = 1
        for j in xrange(0, num_digits):
            product *= int(file_content[j+i])
        if product > result:
            result = product
    return result


if __name__ == '__main__':
    main()
