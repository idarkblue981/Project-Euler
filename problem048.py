"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""


def main():
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    print(sum%10**10)

if __name__ == '__main__':
    main()