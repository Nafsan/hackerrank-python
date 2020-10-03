#!/bin/python3

import os
import sys
import math
#
# Complete the pageCount function below.
#
def pageCount(n, p):
    # from front
    front = math.floor(p/2)
    # print(front)
    # from back
    if n % 2 == 1:
        n -= 1
    if n - p >= 0:
        back = math.ceil((n-p)/2)
        # print(back)
        return min(front, back)
    else:
        return 0

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print(str(result))
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
