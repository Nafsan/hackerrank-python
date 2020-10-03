ara = []
for _ in range(int(input())):
    operation = input().split()
    # print(operation)
    if operation[0] == 'insert':
        ara.insert(int(operation[1]), int(operation[2]))
    elif operation[0] == 'remove':
        ara.remove(int(operation[1]))
    elif operation[0] == 'append':
        ara.append(int(operation[1]))
    elif operation[0] == 'pop':
        ara.pop()
    elif operation[0] == 'sort':
        ara.sort()
    elif operation[0] == 'reverse':
        ara.reverse()
    elif operation[0] == 'print':
        print(ara)
