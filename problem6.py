"""
The sum of the squares of the first ten natural numbers is, 1 ^ 2 + 2 ^ 2 + ... + 10 ^ 2 = 385. 
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10) ^ 2 = 55 ^ 2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():
    r1 = squares_of_the_first_one_hundred()
    r2 = square_of_the_sum()
    calc(r1, r2)

def squares_of_the_first_one_hundred():
    r1 = 0
    for i in range(1, 101):
        r1 = r1 + i ** 2
    return r1

def square_of_the_sum():
    r2 = 0
    sum = 0
    for a in range(1, 101):
        sum = sum + a
    r2 = sum ** 2
    return r2

def calc(r1, r2):
    print(r2 - r1)

if __name__ == '__main__':
    main()