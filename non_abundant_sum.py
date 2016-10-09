import math

cache = set()

def get_non_abundant_sums():
	min_number = 24
	max_number = 28123
	result = 0

	for num in xrange(min_number, max_number+1):
		if is_sum_of_two_abundant(num) == False:
			result += num
			print "non ab. num:", num
	return result

def is_sum_of_two_abundant(num):
	min_abundant = 12
	max_abundant = num - min_abundant

	for i in xrange(min_abundant, max_abundant+1):
		j = num - i
		if (i < min_abundant or j < min_abundant):
			continue
		if is_abundant(i) and is_abundant(j):
			return True
	return False

def is_abundant(num):
	if num in cache:
		return True
	num_sum = 0
	last_divisor = int(math.sqrt(num))
	is_abundant = False
	
	for i in xrange(2, last_divisor+1):
		if num % i == 0:
			num_sum += i
			num_sum += (num / i)
			is_abundant = num_sum > num
	                if is_abundant:
				cache.add(num)
				return True
	return is_abundant


def main():
	print "sum of non-abundant numbers:", get_non_abundant_sums()

if __name__ == "__main__":
	main()

