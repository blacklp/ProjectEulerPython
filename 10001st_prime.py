import math

def main():
    result = generate_nth_prime(10001)
    print result

def generate_nth_prime(n):
    current = 1
    num_primes = 0
    while num_primes < n:
        current+=1
        if is_prime(current):
            num_primes+=1
    return current

def is_prime(n):
    i = 2
    while (i <= math.sqrt(n)):
        if n % i == 0:
            return False
        i+=1
    return True

if __name__ == "__main__":
    main()
