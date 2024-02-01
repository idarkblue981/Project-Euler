"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the 10.001th prime number?
"""


def main():
    count = 0
    number = 1

    while count < 10001:
        number += 1
        prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            count += 1

    print(number)

if __name__ == "__main__":
    main()
