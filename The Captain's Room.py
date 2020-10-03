k = int(input())
ara = list(map(int, input().strip().split()))
ara.sort()
length = len(ara)
if ara[0] != ara[1]:
    print(ara[0])
else:
    for i in range(1, length):
        if i != length-1:
            if ara[i] != ara[i-1] and ara[i] != ara[i+1]:
                print(ara[i])
                break
        else:
            print(ara[i])