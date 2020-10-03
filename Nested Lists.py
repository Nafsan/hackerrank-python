ara = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    ara.append([name, score])

grades = []
for i in range(len(ara)):
    grades.append(ara[i][1])
lowest = min(grades)
for i in range(len(grades)):
    if grades[i] == lowest:
        grades[i] = max(grades)
lowest = min(grades)
answer = []
for i in range(len(ara)):
    if ara[i][1] == lowest:
        answer.append(ara[i][0])
answer.sort()
for i in range(len(answer)):
    ans = str(answer[i])
    for j in range(len(ans)):
        if ans[j].isalnum() is True:
            print(ans[j], end='')
    print()
