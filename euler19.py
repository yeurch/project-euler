# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some
# research for yourself.
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

import time

start = time.time()

def month_length(month, year):
    month_lengths = (31,28,31,30,31,30,31,31,30,31,30,31)
    result = month_lengths[month-1]
    if month == 2 and year % 4 == 0 and (year % 100 > 0 or year % 400 == 0):
        result += 1 # leap year
    return result

year = 1900
month = 1
day_of_week = 1

first_sunday_count = 0
while year < 2001:
    day_of_week = (day_of_week + month_length(month, year)) % 7
    if year >= 1901 and day_of_week == 0:
        first_sunday_count += 1
    month += 1
    if month == 13:
        month = 1
        year += 1
    

print ('Solution is {}'.format(first_sunday_count))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
