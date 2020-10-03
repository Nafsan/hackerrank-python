from collections import Counter

n = int(input())
ara1 = list(map(int, input().strip().split()))
m = int(input())
ara2 = list(map(int, input().strip().split()))
for i in range(m):
    ara1.append(ara2[i])
ara1.sort()
ans = 0
for i in range(len(ara1)):
    if ara1.count(ara1[i]) == 1:
        ans += 1

print(ans)
