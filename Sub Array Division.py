#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        total = s[i]
        for j in range(i+1, i+m):
            if j <len(s):
                total += s[j]
        if total == d:
            count += 1
        # print(total)
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(str(result))
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
