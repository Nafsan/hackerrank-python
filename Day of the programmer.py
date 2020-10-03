#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def julian_leap_year(year):
    if year % 4 == 0:
        return True
    return False


def gregorian_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False


def dayOfProgrammer(year):
    if year < 1918:
        if julian_leap_year(year):
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    elif year > 1918:
        if gregorian_leap_year(year):
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    else:
        return '26.09.'+str(year)

# after 1919:
# leap year = 12.09.year , not leap year = 13.09.year
# before 1919:
# leap year = 30.08.year , not leap year = 31.08.year
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
