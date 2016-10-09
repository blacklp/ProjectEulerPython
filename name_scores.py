def main():
    f = open('p022_names.txt', 'r')
    as_str = f.read()
    as_arr = as_str.split(',')
    as_arr = [elem.replace('\"', '') for elem in as_arr]
    as_arr = sorted(as_arr)
    total_score = get_total_score(as_arr)
    print total_score


def get_total_score(array):
    total = 0
    index = 1
    for name in array:
        score = calculate_name_score(name)
        total += (score * index)
        index += 1
    return total


def calculate_name_score(name):
    score = 0
    for letter in list(name):
        letter_score = get_letter_score(letter)
        score += letter_score
    return score


def get_letter_score(letter):
    return ord(letter) - ord('A') + 1


if __name__ == '__main__':
    main()
