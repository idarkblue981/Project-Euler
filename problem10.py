"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million. 
"""


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_below_limit(limit):
    prime_sum = 0
    for number in range(2, limit):
        if is_prime(number):
            prime_sum += number
    return prime_sum

if __name__ == "__main__":
    limit = 2000000
    result = sum_of_primes_below_limit(limit)
    print(result)