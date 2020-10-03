#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[len(s) - 2] == 'P':
        hr = s.split(':')
        # print(hr)
        hr[0] = str((int(hr[0]) + 12) % 24)
        if len(hr[0]) == 1:
            hr[0] = '0' + hr[0]
        # print(hr)
        string = ':'
        string = string.join(hr)
        # print(string[:len(string)-2])
        return string[:len(string)-2]
    else:
        return s


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    #
    # f.write(result + '\n')
    #
    # f.close()
    print(result)
