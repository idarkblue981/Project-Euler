"""
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


import datetime

def main(start_year, end_year):
    count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            day = datetime.date(year, month, 1)
            if day.weekday() == 6:
                count += 1
    return count

if __name__ == "__main__":
    sundays_count = main(1901, 2000)
    print(sundays_count)
