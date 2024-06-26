"""
n! means n * (n - 1) * ... * 3 * 2 * 1.
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =  27.
Find the sum of the digits in the number 100!.
"""


from math import factorial

def main():
    result = 0
    number = factorial(100)

    for digit in str(number):
        result += int(digit)

    print(result)

if __name__ == '__main__':
    main()
