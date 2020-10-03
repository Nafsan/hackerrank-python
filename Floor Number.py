import math

for _ in range(int(input())):
    n, x = map(int, input().split())
    count = math.ceil((n-2)/x)
    if count < 0:
        count = 1
    else:
        count += 1
    print(count)
