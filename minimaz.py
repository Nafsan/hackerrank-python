#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = sum(arr)
    maxx = total - min(arr)
    minn = total - max(arr)
    print(minn, end=' ')
    print(maxx)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
