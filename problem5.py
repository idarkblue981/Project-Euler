"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any reminder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
"""


import math

def main():
    lcm = 1
    limit = 20

    for i in range(1, limit + 1):
        lcm = (lcm * i) // math.gcd(lcm, i)

    result = lcm
    print(result)

if __name__ == "__main__":
    main()