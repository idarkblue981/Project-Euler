"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""


def main():
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    total_letters = 0

    for i in range(1, 1001):
        if 1 <= i < 20:
            word = ones[i]
        elif 20 <= i < 100:
            word = tens[i // 10] + ones[i % 10]
        elif 100 <= i < 1000:
            if i % 100 == 0:
                word = ones[i // 100] + "hundred"
            else:
                if 1 <= (i % 100) < 20:
                    word = ones[i // 100] + "hundredand" + ones[i % 100]
                else:
                    word = ones[i // 100] + "hundredand" + tens[(i % 100) // 10] + ones[(i % 100) % 10]
        elif i == 1000:
            word = "onethousand"
        else:
            word = "invalid"

        total_letters += len(word)

    print(total_letters)

if __name__ == '__main__':
    main()