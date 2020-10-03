n = int(input())
ara = list(map(int, input().strip().split()))
ara.sort()
highest = max(ara)
max_index = ara.index(highest)
if max_index == 0:
    print(highest)
else:
    print(ara[max_index-1])
