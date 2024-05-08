"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def main():
    x = 1
    while True:
        if all(has_same_digits(x, i) for i in range(2, 7)):
            print(x)
            break
        else:
            x += 1

def has_same_digits(x, multiple):
    digits_x = sorted(str(x))
    digits_multiple = sorted(str(x * multiple))
    return digits_x == digits_multiple

if __name__ == '__main__':
    main()