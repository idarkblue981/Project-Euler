"""
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?
"""


def main():
    with open("names.txt", "r") as file:
        names_content = file.read()

    names_list = sorted(name.strip('"') for name in names_content.split(','))

    result = total_name_scores(names_list)
    print(result)

def alphabetical_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

def total_name_scores(names):
    total_score = 0
    for i, name in enumerate(names, start=1):
        score = alphabetical_value(name) * i
        total_score += score
    return total_score

if __name__ == "__main__":
    main()
