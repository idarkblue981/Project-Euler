"""
The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def find_starting_number_with_longest_chain(limit):
    max_length = 0
    starting_number = 0

    for i in range(2, limit):
        current_length = collatz_sequence_length(i)
        if current_length > max_length:
            max_length = current_length
            starting_number = i

    return starting_number

if __name__ == "__main__":
    limit = 1000000
    result = find_starting_number_with_longest_chain(limit)
    print(result)