"""
A googol (10 ** 100) is a massive number: one followed by one-hundred zeros; 100 ** 100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a ** b, where a, b < 100, what is the maximum digital sum?
"""


def main():
    max_sum = 0

    for a in range(1, 100):
        for b in range(1, 100):
            result = 0
            temp = a ** b
            while temp:
                result += temp % 10
                temp //= 10

            if result > max_sum:
                max_sum = result

    print(max_sum)

if __name__ == '__main__':
    main()