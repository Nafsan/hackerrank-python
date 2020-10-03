#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = minn = ans = down_so_far = 0
    for i in range(steps):
        if path[i] == 'U':
            count += 1
            down_so_far = 0
        else:
            down_so_far += 1
            count -= 1
            if count < -1 and down_so_far > 1:
                if i + 1 != steps and path[i + 1] == 'U':
                    ans += 1
    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(str(result))
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
