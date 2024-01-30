"""
The prime factors of 13195 are 5, 7, 13 and 29. 
What is the largest prime factor of the number 600851475143?
"""


def main():
    limit = 600851475143
    factor = 2

    while factor * factor <= limit:
        if limit % factor == 0:
            limit //= factor
        else:
            factor += 1

    result = limit
    print(result)

if __name__ == "__main__":
    main()