x = int(input())
y = int(input())
z = int(input())
n = int(input())
ara = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            dummy = [i, j, k]
            ara.append(dummy)
ans = [i for i in ara if sum(i) != n]
print(ans)

