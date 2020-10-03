n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
ans = student_marks.get(query_name)
answer = sum(ans) / len(ans)
print("%.2f" % answer)
