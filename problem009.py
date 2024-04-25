"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def find_pythagorean_triplet(sum_target):
    for a in range(1, sum_target // 3):
        for b in range(a + 1, sum_target // 2):
            c = sum_target - a - b
            if a**2 + b**2 == c**2:
                return a, b, c

def main():
    sum_target = 1000
    triplet = find_pythagorean_triplet(sum_target)

    if triplet:
        a, b, c = triplet
        product_abc = a * b * c
        print(product_abc)

if __name__ == '__main__':
    main()
