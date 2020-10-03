for _ in range(int(input())):
    n = int(input())
    ara1 = list(map(int, input().strip().split()))
    m = int(input())
    ara2 = list(map(int, input().strip().split()))
    ara1.sort()
    ara2.sort()
    flag = 0
    for i in range(n):
        if ara2.count(ara1[i]) > 0:
            flag = 1
        else:
            flag = 0
            break
    if flag == 0:
        print('False')
    else:
        print('True')
