def swap_case(s):
    ara = []
    for i in range(len(s)):
        if s[i].isupper() is True:
            ara.append(s[i].lower())
        else:
            ara.append(s[i].upper())
    string = ''.join(ara)
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
