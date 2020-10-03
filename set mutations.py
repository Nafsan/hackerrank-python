t = int(input())
ara = set(map(int, input().strip().split()))

for _ in range(int(input())):
    operation, n = input().split()
    ara2 = set(map(int, input().strip().split()))
    if operation == 'intersection_update':
        ara.intersection_update(ara2)
    if operation == 'symmetric_difference_update':
        ara.symmetric_difference_update(ara2)
    if operation == 'difference_update':
        ara.difference_update(ara2)
    if operation == 'update':
        ara.update(ara2)
answer = 0
for i in ara:
    answer += i
print(answer)