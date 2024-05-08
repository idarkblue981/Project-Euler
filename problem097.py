"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form s ** 6972593 - 1; 
it contains exactly 2098086 digits. Subsequently other Mersenne primes, of the form 2 ** p - 1, have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 2357207 digits: 28433 * 2 ** 7830457 + 1.
Find the last ten digits of this prime number.
"""


def main():
    number = 28433 * (2 ** 7830457) + 1
    print(number%10**10)

if __name__ == '__main__':
    main()