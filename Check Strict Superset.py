ara = list(map(int, input().strip().split()))
n = int(input())
ara.sort()
check = []
for i in range(n):
    ara2 = list(map(int, input().strip().split()))
    ara2.sort()
    flag = 0
    # flag = 0 ---> True
    # flag = 1 ---> False
    if len(ara) == len(ara2):
        flag = 1
    else:
        for j in range(len(ara2)):
            if ara.count(ara2[j]) > 0:
                flag = 0
            else:
                flag = 1
                break
    check.append(flag)
check.sort()
check.reverse()
if check[0] == 0:
    print('True')
else:
    print('False')
