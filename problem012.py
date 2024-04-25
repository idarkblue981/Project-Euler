"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be: 
1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...
Let us list the factors of the first seven triangle numbers:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""


def prime_factors_count(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def count_divisors(n):
    factors = prime_factors_count(n)
    result = 1
    for factor in factors.values():
        result *= (factor + 1)
    return result

def find_triangle_number_with_divisors(divisor_limit):
    n = 1
    triangle_number = 1

    while count_divisors(triangle_number) <= divisor_limit:
        n += 1
        triangle_number += n

    return triangle_number

if __name__ == "__main__":
    divisor_limit = 500
    result = find_triangle_number_with_divisors(divisor_limit)
    print(result)