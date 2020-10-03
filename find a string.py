def count_substring(string, sub_string):
    len_substring = len(sub_string)
    cnt = total = i = 0
    while i != len(string):
        if string[i] == sub_string[cnt]:
            cnt += 1
            i += 1
        else:
            cnt = 0
            i += 1
        if cnt == len_substring:
            total += 1
            cnt = 0
            i -= len_substring - 1
    return total


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)