#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freq = {}
    for i in ar:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    total = 0
    for i in freq:
        total += freq[i] // 2
    return total


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
