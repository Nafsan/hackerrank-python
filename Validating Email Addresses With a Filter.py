ok = 1
not_ok = 0


def check_username(string):
    result = 0
    for j in range(len(string)):
        if string[j] == '-' or string[j] == '_' or '0' <= string[j] <= '9' or 'A' <= string[j] <= 'Z' or 'a' <= string[
            j] <= 'z':
            result = ok
        else:
            result = not_ok
            break
    return result


def check_web(string):
    result = 0
    for j in range(len(string)):
        if '0' <= string[j] <= '9' or 'a' <= string[j] <= 'z' or 'A' <= string[j] <= 'Z':
            result = ok
        else:
            result = not_ok
    return result


ara = []
for _ in range(int(input())):
    email = input()
    username = web = extension = ''
    flag = 0
    index = 0
    for i in range(len(email)):
        if email[i] == '@':
            flag = 1
            index = i
            break
        username += email[i]

    if flag == 1:
        for i in range(index + 1, len(email)):
            if email[i] == '.':
                flag = 2
                index = i
                break
            web += email[i]
    if flag == 2:
        for i in range(index + 1, len(email)):
            extension += email[i]
        if len(extension) == 3:
            flag += 1

    if flag == 3:
        if check_username(username) == 1 and check_web(web) == 1:
            ara.append(email)
ara.sort()
print(ara)
